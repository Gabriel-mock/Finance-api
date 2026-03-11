# Finance API

A personal finance REST API built with **FastAPI** that allows users to securely track income, expenses, budgets, and financial summaries. The API includes authentication using JWT tokens and provides interactive documentation through Swagger UI.

---

## Overview

This project is a backend service designed to help users manage their personal finances through a RESTful API. It demonstrates backend development concepts such as authentication, database management, API design, and modular project structure using modern Python tools.

---

## Features

* User registration and login with **JWT authentication**
* Income tracking
* Expense tracking
* Budget management
* Financial summaries
* Interactive API documentation with **Swagger UI**

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Uvicorn
* Docker

---

## Live Demo

* **API Base URL:**
  https://finance-api-5ydp.onrender.com

* **API Documentation:**
  https://finance-api-5ydp.onrender.com/docs

---

## Architecture

* **Frontend** – Dashboard / Web App
* **Backend** – FastAPI API server
* **Authentication** – JWT tokens
* **Database** – SQLite with SQLAlchemy ORM

---

## API Endpoints

### Authentication

* `POST /register` – Create a new user account
* `POST /login` – Authenticate user and receive a JWT token

### Income

* `GET /income` – Retrieve all income records
* `POST /income` – Add a new income record

### Expenses

* `GET /expenses` – Retrieve all expense records
* `POST /expenses` – Add a new expense record

### Budget

* `GET /budget` – View budget data
* `POST /budget` – Create or update a budget

### Summary

* `GET /summary` – View financial summary data

---

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

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/Gabriel-mock/Finance-api.git
cd Finance-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* Add categories for income and expenses
* Add analytics and financial charts
* Improve automated test coverage
* Add PostgreSQL support for production environments
