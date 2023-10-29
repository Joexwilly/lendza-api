from sqlalchemy.orm import Session 
from schemas.loan import CreateLoan, ShowLoan
from db.models.loan import SubmitLoan


def create_new_loan(loan: CreateLoan, db: Session, author_id: int):
    loan = SubmitLoan(
        reference = loan.reference,
        amount = loan.amount,
        duration = loan.duration,
        interest_rate = loan.interest_rate,
        content = loan.content,
        
        
         author_id=author_id)
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan





