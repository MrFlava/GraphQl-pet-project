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

    def add_post(self, post_data: PostInput):
        user = User.find(post_data.user_id)

        if not user:
            raise Exception(f"User {post_data.user_id} does not exist")

        post = Post()
        post.user_id = user.id
        post.title = post_data.title
        post.description = post_data.description

        post.save()
        return post

class Queries:

    def get_all_users(self) -> List[UserType]:
        return User.all()

    def get_single_user(self, user_id: int) -> UserType:
        user = User.find(user_id)
        if not user:
            raise Exception("User not found")
        return user