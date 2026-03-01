from pydantic import BaseModel, Field

class BudgetUpdate(BaseModel):
    monthly_budget: float = Field(..., gt=0)