import crypt
from typing import List

from db.models import Post, User
from db.schemas import PostInput, PostType, UserInput, UserType


class CreateMutation:

    def add_user(self, user_data: UserInput):
        user = User.where("username", user_data.username).get()

        if user:
            raise Exception(f"User {user_data.username} already exists")

        user = User()

        user.username = user_data.username
        user.password = crypt.crypt(user_data.password)

        user.save()

        return user