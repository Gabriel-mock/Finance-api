# Finance API

A personal finance REST API built with **FastAPI** for user authentication, income tracking, expense tracking, budgeting, and financial summaries.

## Overview

This project is a backend service that allows users to securely track their finances through a RESTful API. It demonstrates backend development concepts such as authentication, database management, API design, and modular project structure.

## Features

- User registration and login with JWT authentication
- Income tracking
- Expense tracking
- Budget management
- Financial summaries
- Interactive API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Docker

## Live Demo

- **API:** https://finance-api-5ydp.onrender.com  
- **Docs:** https://finance-api-5ydp.onrender.com/docs  

## API Documentation

![API Docs](images/api-docs.png)

## Architecture

- **Frontend** – Dashboard / Web App
- **Backend** – FastAPI API server
- **Authentication** – JWT tokens
- **Database** – SQLite with SQLAlchemy ORM

## API Endpoints

### Auth
- `POST /register` – Create a new user account
- `POST /login` – Log in and receive a JWT token

### Income
- `GET /income` – View all income records
- `POST /income` – Add a new income record

### Expenses
- `GET /expenses` – View all expense records
- `POST /expenses` – Add a new expense record

### Budget
- `GET /budget` – View budget data
- `POST /budget` – Create or update a budget

### Summary
- `GET /summary` – View financial summary

## Project Structure  
routers/
models/
schemas/
tests/
main.py
database.py
security.py

```bash
git clone https://github.com/Gabriel-mock/Finance-api.git
cd Finance-api
pip install -r requirements.txt
uvicorn main:app --reload
