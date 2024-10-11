from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from modules.user.enums import Genders, Belt, AddressType


class UserAddressCreate(BaseModel):
    address: str
    city: str
    postal_code: str
    address_type: AddressType


class UserAddress(UserAddressCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    first_name: str
    last_name: str
    aka_name: str
    birth_date: datetime
    gender_code: Genders
    phone_mom: str
    phone_dad: str
    mom_name: str
    dad_name: str
    active: bool
    belt: Belt
    notes: Optional[str]



class UserCreate(UserBase):
    pass


class UserUpsert(UserBase):
    id: Optional[int]



class User(UserBase):
    id: int
    address: list[UserAddress] = []

    class Config:
        orm_mode = True
