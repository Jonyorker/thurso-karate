from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Enum as ENUM
from sqlalchemy import ForeignKey, Integer, UnicodeText, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float

from database.database import Base
from modules.user.enums import Genders, Belt, AddressType


def make_timestamptz() -> DateTime:
    return DateTime(timezone=True)


class CreatedAtMixin:
    created_at = Column(
        make_timestamptz(),
        server_default=func.current_timestamp(),
        nullable=False,
        doc="Time at which the row was created.",
    )


class UpdatedAtMixin:
    updated_at = Column(
        make_timestamptz(),
        server_default=func.current_timestamp(),
        onupdate=datetime.utcnow,
        nullable=False,
        doc="Time at which the row was updated.",
    )


class CreatedAtUpdatedAtMixin(CreatedAtMixin, UpdatedAtMixin):
    pass


def make_enum(enum_cls) -> ENUM:
    """Helper class to create an enum column that is stored as a VARCHAR"""
    return ENUM(
        enum_cls,
        create_constraint=False,
        native_enum=False,
        length=255,
    )


class User(CreatedAtMixin, Base):
    __tablename__ = "user_list"
    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(UnicodeText, nullable=False)
    last_name: str = Column(UnicodeText, nullable=False)
    aka_name: str = Column(UnicodeText, nullable=True)
    birth_date: datetime = Column(DateTime, nullable=False)
    gender_code: Genders = Column(make_enum(Genders), nullable=False)
    phone_mom: str = Column(UnicodeText, nullable=True)
    phone_dad: str = Column(UnicodeText, nullable=True)
    mom_name: str = Column(UnicodeText, nullable=True)
    dad_name: str = Column(UnicodeText, nullable=True)
    active: bool = Column(Boolean, nullable=False, default=True)
    belt: Belt = Column(make_enum(Genders), nullable=False)
    notes: str = Column(UnicodeText, nullable=True)
    address = relationship("UserAddress", back_populates="user")


class UserAddress(CreatedAtMixin, Base):
    __tablename__ = "user_address"
    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("user_list.id"), nullable=False)
    address: str = Column(UnicodeText, nullable=False)
    city: str = Column(UnicodeText, nullable=False)
    province: str = Column(UnicodeText, nullable=False)
    postal_code: str = Column(UnicodeText, nullable=False)
    address_type: AddressType = Column(make_enum(AddressType), nullable=False)
    user = relationship("User", back_populates="address")
