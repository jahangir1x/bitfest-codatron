# 🚀 fastapi-hackathonkit

![Badge](https://img.shields.io/badge/Made%20with-FastAPI-green) ![Badge](https://img.shields.io/badge/PostgreSQL-For%20All%20Your%20Data%20Needs-blue) ![Badge](https://img.shields.io/badge/Dockerized-Yep!-2496ED) ![Badge](https://img.shields.io/badge/Forked-But%20Revamped-red)

## Setup & Run 🏃‍♂️

- Clone this repository:
```bash
git clone https://github.com/jahangir1x/fastapi-hackathonkit.git
```

- Set up your environment by copying the template .env file:
```bash
cd fastapi-hackathonkit

cp dot-env-template .env   # linux
copy dot-env-template .env # windows
```

- For local development
```bash
python -m venv .pyenv

source .pyenv/bin/activate # linux
.pyenv\Scripts\activate     # windows

pip install -r requirements.txt

export PYTHONPATH=$PWD # linux
set PYTHONPATH=%cd%    # windows

# make sure your postgresql server is running
python app/check_db_connection.py
alembic upgrade head
python app/seed_db_with_initial_data.py
fastapi dev app/main.py --reload
```

- For Docker
```bash
docker-compose up --build
```

## Workflow 🛠 ️
##### Define models
- Edit `app/models/{new_item}.py`
- Then we need to register the model in `app/models/__init__.py`
##### Create revision for the model
- create revision file with `$ alembic revision --autogenerate -m "Add {new_item} table"`
- then upgrade the database with `$ alembic upgrade head`
##### Add some dummy data in the database.
- Open any database client and add some data in the table.
##### Define schemas
- Edit `app/schemas/{new_item}.py`
- Then we need to register the schema in `app/schemas/__init__.py`
##### Define CRUD operations
- Edit `app/crud/{new_item}.py`
- Then we need to register the crud in `app/crud/__init__.py`
##### Define API endpoints
- Edit `app/api/api_v{x}/{new_item}.py`
- Then we need to register the router in `app/api/api_v{x}/api.py`
