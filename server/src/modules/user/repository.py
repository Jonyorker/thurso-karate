from typing import List
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from database.database import get_db
from modules.user import model, schema


class UserRepository:
    def __init__(self):
        generator = get_db()
        self.db: Session = next(generator)

    def get_user(self, user_id: int) -> schema.User:
        # Showcase of the query api, which is very fast, flexible and intelligent in loading relations
        # if the object return type includes it.
        return self.db.query(model.User).filter(model.User.id == user_id).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> List[schema.User]:
        return self.db.query(model.User).offset(skip).limit(limit).all()

    def create_user(self, user: schema.UserCreate) -> schema.User:
        db_user = model.User(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def upsert_user(self, user: schema.UserUpsert) -> schema.User:
        # Showcase of the session api, which is more flexible for complex queries/actions
        stmt = (
            insert(model.User)
            .values(user.dict())
            .on_conflict_do_update(index_elements=[model.User.id], set_=user.dict())
        )

        self.db.execute(stmt)
        self.db.commit()

        # Upserts do not return the row they modified, so we must call once more if we want to return an object.
        # Typically, Upsets shine with bulk updates or consumers from Kafka/Rabbit

        return self.get_user(user.id)

    def create_user_address(
        self, user_id: int, address: schema.UserAddressCreate
    ) -> schema.UserAddress:
        db_user = self.get_user(user_id=user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")

        db_user_address = model.UserAddress(**address.model_dump())
        db_user_address.user_id = user_id
        db_user_address.province = 'QC'
        self.db.add(db_user_address)
        self.db.commit()
        self.db.refresh(db_user_address)
        return db_user_address

    def create_user_from_seed(self, user) -> schema.User:
        db_user = model.User(**user)
        db_user.uuid = uuid4()
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def create_user_address_from_seed(self, user_address) -> schema.UserAddress:
        db_user_address = model.UserAddress(**user_address)
        self.db.add(db_user_address)
        self.db.commit()
        self.db.refresh(db_user_address)
        return db_user_address
