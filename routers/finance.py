from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models.income import Income
from models.expense import Expense
from models.user import User
from schemas.income import IncomeCreate, IncomeResponse
from schemas.expense import ExpenseCreate, ExpenseResponse
from schemas.summary import SummaryResponse
from dependencies import get_current_user
from schemas.budget import BudgetUpdate

router = APIRouter()


@router.post("/income", response_model=IncomeResponse)
def create_income(
    income: IncomeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_income = Income(
        amount=income.amount,
        description=income.description,
        user_id=current_user.id
    )

    db.add(new_income)
    db.commit()
    db.refresh(new_income)

    return new_income


@router.get("/income/{income_id}", response_model=IncomeResponse)
def get_income_by_id(
    income_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()

    if not income:
        raise HTTPException(status_code=404, detail="Income not found")

    return income


@router.get("/summary", response_model=SummaryResponse)
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total_income = db.query(func.sum(Income.amount)).filter(
        Income.user_id == current_user.id
    ).scalar() or 0

    total_expense = db.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id
    ).scalar() or 0

    balance = total_income - total_expense

    budget_limit = current_user.monthly_budget
    budget_exceeded = False

    if budget_limit is not None:
        budget_exceeded = total_expense > budget_limit

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "budget_limit": budget_limit,
        "budget_exceeded": budget_exceeded
    }
    


@router.put("/expense/{expense_id}", response_model=ExpenseResponse)
def update_expense(
    expense_id: int,
    expense_update: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == current_user.id
    ).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense.amount = expense_update.amount
    expense.description = expense_update.description

    db.commit()
    db.refresh(expense)

    return expense

@router.get("/income", response_model=list[IncomeResponse])
def get_all_income(
    limit: int = 10,
    offset: int = 0,
    min_amount: float | None = None,
    max_amount: float | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Income).filter(
        Income.user_id == current_user.id
    )

    if min_amount is not None:
        query = query.filter(Income.amount >= min_amount)

    if max_amount is not None:
        query = query.filter(Income.amount <= max_amount)

    incomes = query.offset(offset).limit(limit).all()

    return incomes

@router.put("/income/{income_id}", response_model=IncomeResponse)
def update_income(
    income_id: int,
    income_update: IncomeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()

    if not income:
        raise HTTPException(status_code=404, detail="Income not found")

    income.amount = income_update.amount
    income.description = income_update.description

    db.commit()
    db.refresh(income)

    return income

@router.delete("/income/{income_id}")
def delete_income(
    income_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()

    if not income:
        raise HTTPException(status_code=404, detail="Income not found")

    db.delete(income)
    db.commit()

    return {"message": "Income deleted successfully"}

@router.get("/expense", response_model=list[ExpenseResponse])
def get_all_expenses(
    limit: int = 10,
    offset: int = 0,
    min_amount: float | None = None,
    max_amount: float | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Expense).filter(
        Expense.user_id == current_user.id
    )

    if min_amount is not None:
        query = query.filter(Expense.amount >= min_amount)

    if max_amount is not None:
        query = query.filter(Expense.amount <= max_amount)

    expenses = query.offset(offset).limit(limit).all()

    return expenses

@router.delete("/expense/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == current_user.id
    ).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}

@router.put("/budget")
def update_budget(
    budget: BudgetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    current_user.monthly_budget = budget.monthly_budget
    db.commit()
    db.refresh(current_user)

    return {"message": "Budget updated successfully"}

@router.post("/expense", response_model=ExpenseResponse)
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_expense = Expense(
        amount=expense.amount,
        description=expense.description,
        user_id=current_user.id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense