from pydantic import BaseModel, Field
from typing import Optional

class IncomeCreate(BaseModel):
    amount: float = Field(..., gt=0)
    description: Optional[str] = None

class IncomeResponse(BaseModel):
    id: int
    amount: float
    description: Optional[str]

    class Config:
        orm_mode = True