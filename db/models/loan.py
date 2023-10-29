from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey, Float, Interval
from sqlalchemy.orm import relationship

from db.base_class import Base


class SubmitLoan(Base):
    id = Column(Integer, primary_key=True)
 #interest rate column as float
    interest_rate = Column(Float, nullable=False)
    reference = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id =  Column(Integer,ForeignKey("user.id"))
    author = relationship("User",back_populates="loans")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
    #duration coloumn using datetime
    duration = Column(Interval, nullable=False)


