from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from db.repository.loan import create_new_loan
from db.session import get_db
from typing import List
from schemas.loan import CreateLoan, ShowLoan


router = APIRouter()


@router.post("/loan",response_model=ShowLoan, status_code=status.HTTP_201_CREATED)
async def submit_loan(loan: CreateLoan, db: Session= Depends(get_db)):
    loan = create_new_loan(loan=loan, db=db)
    return loan