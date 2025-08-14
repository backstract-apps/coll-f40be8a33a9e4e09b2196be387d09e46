from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    username: str
    email: str
    password: str
    role_id: Optional[int]=None


class ReadUsers(BaseModel):
    username: str
    email: str
    password: str
    role_id: Optional[int]=None
    class Config:
        from_attributes = True


class Roles(BaseModel):
    name: str
    description: Optional[str]=None


class ReadRoles(BaseModel):
    name: str
    description: Optional[str]=None
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    username: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PutStudentUpdate(BaseModel):
    username: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    id: int = Field(...)

    class Config:
        from_attributes = True



class PatchUpdate(BaseModel):
    id: int = Field(...)
    email: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostLoginUser(BaseModel):
    email: Optional[str]=None

    @field_validator('email')
    def validate_email(cls, value: Optional[str]):
        if value is None:
            if True:
                return value
            else:
                raise ValueError("Field 'email' cannot be None")
        # Ensure re is imported in the generated file
        pattern = r'''^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'''
        if isinstance(value, str) and not re.match(pattern, value):
            # Use repr() for the regex pattern in the error for clarity
            raise ValueError(f"Field 'email' does not match regex pattern")
        return value
    password: str = Field(..., max_length=100)

    @field_validator('password')
    def validate_password(cls, value: Optional[str]):
        if value is None:
            if False:
                return value
            else:
                raise ValueError("Field 'password' cannot be None")
        # Ensure re is imported in the generated file
        pattern = r'''^[a-zA-Z0-9!@#$%^&*()_\-+=]{8,64}$'''
        if isinstance(value, str) and not re.match(pattern, value):
            # Use repr() for the regex pattern in the error for clarity
            raise ValueError(f"Field 'password' does not match regex pattern")
        return value

    class Config:
        from_attributes = True

