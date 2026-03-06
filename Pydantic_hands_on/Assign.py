from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict
from typing import Dict, Optional

class Address(BaseModel):
    city : str = Field(min_length=3)
    pincode : str = Field(len=6)

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls,pin):
        if len(pin) != 6:
            raise ValueError("Pincode must be of 6 digits")
        return pin

class User(BaseModel):
    user_id : int
    name : str
    email : EmailStr
    age : int 
    address : Address
    is_premium : Optional[bool] = Field(default=False)

    @field_validator("age")
    @classmethod
    def validate_pincode(cls,a):
        if a <= 18:
            raise ValueError("User must be at least 18 years old")
        return a

address_info = {"city" : "ghaziabad","pincode": "123456"}
address_obj = Address(**address_info)

user_info = {"user_id" : 123,"name": "Kanika", "email":"kanikamalik44@gmail.com","age":32,"address":address_obj}
user_obj = User(**user_info)

print(user_obj.age)
