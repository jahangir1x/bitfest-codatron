import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader,TextLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS


from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

ingredients = 'milk, lemon juice, sugar, water, cardamom pods, Mustard oil' 

if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings()
    st.session_state.loader = TextLoader("./recipees/recipees.txt")
    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
    st.session_state.vector = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

st.title("Recipee Demo")
llm = ChatGroq(groq_api_key = groq_api_key,
               model_name='mixtral-8x7b-32768')

prompt = ChatPromptTemplate.from_template(
    """
You are a recipee assistant. Here are the list of ingredients:{ingredients}

 A list of recipees will be given to you as context.Save each user separately. User will tell you his craving and you have to output a recipee according to his craving and which can be made with those ingredients. 
Please provide accurate recipee from the given context which matches user's craving and which can be made using those ingredients.
<context>
{context}
<context>
User: {input}
"""
)
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval = st.session_state.vector.as_retriever()

retrieval_chain = create_retrieval_chain(retrieval, document_chain)

prompt = st.text_input("Input your prompt here")

if prompt:
    response = retrieval_chain.invoke({"input":prompt})
    st.write(response['answer'])