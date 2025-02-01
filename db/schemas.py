from typing import List

from graphene import ObjectType, Field, String, ID, Int
from graphene_sqlalchemy import SQLAlchemyObjectType
from pkg_resources import require

from .db_utils import get_db
from .models import User, Post

class PostNode(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (ObjectType,)

class FilterPostNodesQuery(SQLAlchemyObjectType):
    post = Field(lambda: List[PostNode], limit=Int())

    def resolve_filter_posts(self, info, limit=None):
        query = Post.get_query(info)
        if limit:
            return query.limit(limit).all()
        return query.all()

class CreatePostNode(SQLAlchemyObjectType):
    post = Field(lambda: PostNode)

    class Arguments:
        id = ID(required=True)
        title=String(required=True)
        description=String(require=True)
        user_ud = Int(required=True)

        def mutate(self, info, id, title, description, user_ud):
            pass