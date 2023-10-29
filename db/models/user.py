from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from enum import Enum
from typing import List

#create enum of user roles
class UserRoles(str,Enum):
    lender = "lender"
    borrower = "borrower"
   


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    #add role column and default to borrower
    role = Column(String,nullable=False,default= UserRoles.lender)
    loans = relationship("SubmitLoan",back_populates="author")
    
    
    

    
    



