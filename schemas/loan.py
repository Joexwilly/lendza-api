from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date



class CreateLoan(BaseModel):
    reference: str 
    amount: float
    interest_rate: float
    duration: int
    content: Optional[str] = None 
    
    
class ShowLoan(BaseModel):
    reference: str
    amount: float
    interest_rate: float
    duration: int
    content: Optional[str]
    created_at: date

    class Config():
        from_attributes = True