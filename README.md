# Finance API

A personal finance REST API built with FastAPI for user authentication, income tracking, expense tracking, budgeting, and financial summaries.

## Features

* User registration and login with JWT authentication
* Income tracking
* Expense tracking
* Budget management
* Financial summaries
* API documentation with Swagger UI

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Docker

## Live Demo

* API: https://your-render-link.onrender.com
* Docs: https://your-render-link.onrender.com/docs

## Project Structure

```
routers/
models/
schemas/
tests/
main.py
database.py
security.py
```

## Running Locally

```bash
git clone https://github.com/Gabriel-mock/Finance-api.git
cd Finance-api
pip install -r requirements.txt
uvicorn main:app --reload
```

## Future Improvements

* Add categories for income and expenses
* Add charts and analytics endpoints
* Improve test coverage
* Add PostgreSQL support
