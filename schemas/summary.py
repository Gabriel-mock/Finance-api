from pydantic import BaseModel
from typing import Optional

class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float
    balance: float
    budget_limit: Optional[float] = None
    budget_exceeded: bool