# RecipieSuggestor API Documentation

This document provides an overview of the API endpoints available in the RecipieSuggestor application.

---

## Overview

**API Version:** 0.1.0  
**Base URL:** `/api/v1/`

### Description

The RecipieSuggestor application allows users to manage and retrieve recipes and ingredients efficiently. Here's how it works:

1. **Recipe Management:**
   - Users save their recipes in a text file.
   - The recipe text is sent to the system using a POST request to the `/recipes/` endpoint.
   - The recipe is stored in a vector database associated with an LLM (Large Language Model).

2. **Ingredient Management:**
   - Users can manage ingredients they have through the `/ingredients/` API.
   - If new ingredients are purchased, they are added to the database via a POST request.
   - When ingredients are used in cooking a recipe, they are removed from the database via a DELETE request.

3. **Recipe Suggestions:**
   - Users provide a prompt, such as "I want to cook something sweet," to the `/suggestions/` endpoint.
   - The LLM combines the available ingredients and stored recipes to generate a suitable recipe suggestion.

---


## Endpoints

### Recipes

#### 1. Create Recipe

**Route:** `/recipes/`  
**Method:** `POST`  
**Tags:** `recipes`  

**Description:** Create a new recipe.

**Request Body:**
```json
{
  "details": "string"
}
```

**Response:**
- **200:** Successful Response
  ```json
  {
    "status": "string"
  }
  ```
- **422:** Validation Error
  ```json
  {
    "detail": [
      {
        "loc": ["string", "integer"],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

---

### Ingredients

#### 1. Retrieve Ingredients

**Route:** `/ingredients/`  
**Method:** `GET`  
**Tags:** `ingredients`  

**Description:** Retrieve a list of ingredients.

**Query Parameters:**
- `skip` (integer, default: 0): Number of items to skip.
- `limit` (integer, default: 100): Maximum number of items to retrieve.

**Response:**
- **200:** Successful Response
  ```json
  [
    {
      "id": "integer",
      "name": "string"
    }
  ]
  ```
- **422:** Validation Error
  ```json
  {
    "detail": [
      {
        "loc": ["string", "integer"],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

#### 2. Create Ingredient

**Route:** `/ingredients/`  
**Method:** `POST`  
**Tags:** `ingredients`  

**Description:** Create a new ingredient.

**Request Body:**
```json
{
  "name": "string"
}
```

**Response:**
- **200:** Successful Response
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
- **422:** Validation Error
  ```json
  {
    "detail": [
      {
        "loc": ["string", "integer"],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

#### 3. Delete Ingredient

**Route:** `/ingredients/{id}`  
**Method:** `DELETE`  
**Tags:** `ingredients`  

**Description:** Delete an ingredient by ID.

**Path Parameters:**
- `id` (integer): The ID of the ingredient to delete.

**Response:**
- **200:** Successful Response
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
- **422:** Validation Error
  ```json
  {
    "detail": [
      {
        "loc": ["string", "integer"],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

---

### Suggestions

#### 1. Create Suggestion

**Route:** `/suggestions/`  
**Method:** `POST`  
**Tags:** `suggestions`  

**Description:** Exact Prompt From user

**Request Body:**
```json
{
  "details": "string"
}
```

**Response:**
- **200:** Successful Response
  ```json
  {
    "details": "string"
  }
  ```
- **422:** Validation Error
  ```json
  {
    "detail": [
      {
        "loc": ["string", "integer"],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```

---
