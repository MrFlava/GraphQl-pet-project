import strawberry

from typing import List, Optional

@strawberry.type
class PostType:
    id: int
    user_id: int
    title: str
    description: str


class UserType:
    id: int
    username: str
    password: str
    posts: Optional[List[PostType]]


@strawberry.input
class UserInput:
    username: str
    password: str

@strawberry.input
class PostInput:
    user_id: int
    title: str
    description: str