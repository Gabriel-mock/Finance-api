from pydantic import BaseModel, Field
from typing import Optional

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0)
    description: Optional[str] = None

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    description: Optional[str]

    class Config:
        orm_mode = True