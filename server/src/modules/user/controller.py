from repository import UserRepository
from schema import UserCreate


class UserController:
    def __init__(self):
        pass

    def get_all_users(self):
        return UserRepository().get_users()

    def get_user(self, user_id):
        return UserRepository().get_user(user_id)

    def create_user(self, user):
        return UserRepository().create_user(user)

    def upsert_user(self, user):
        return UserRepository().upsert_user(user)

    def upsert_user_address(self, user_id, address):
        return UserRepository().create_user_address(user_id, address)
