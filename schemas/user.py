from pydantic import BaseModel,EmailStr, Field


#properties required during user creation
class UserCreate(BaseModel):
    first_name : str = Field(...)
    last_name : str = Field(...)
    email : EmailStr
    phone : str = Field(...)
    password : str = Field(..., min_length=4)
    
    
    
    
    
class ShowUser(BaseModel):
    id: int
    email : EmailStr
    first_name : str = Field(...)
    last_name : str = Field(...)
    phone : str = Field(...)
    is_active : bool

    class Config():  #tells pydantic to convert even non dict obj to json
        from_attributes = True