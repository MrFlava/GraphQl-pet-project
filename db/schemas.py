from typing import List

from graphene import ObjectType, Field, String, ID, Int
from graphene_sqlalchemy import SQLAlchemyObjectType
from pkg_resources import require

from .db_utils import get_db
from .models import User, Post

class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (ObjectType,)


class CreateUserNode(SQLAlchemyObjectType):
    class Arguments:
        pass


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
        user_id = Int(required=True)

        def mutate(self, info, id, title, description, user_id):
            db = get_db()
            post = Post(id=id, title=title, description=description, user_id=user_id)
            db.add(post)
            db.commit()
            db.refresh(post)
            return CreatePostNode(post=post)

class UpdatePostNode(SQLAlchemyObjectType):
    post = Field(lambda: PostNode)

    class Arguments:
        id = ID(required=True)
        title=String(required=True)
        description=String(required=True)
        user_id = Int(required=True)

        def mutate(self, info, post_id, title, description, user_id):
            db = get_db()
            post_for_update = Post.query.get(Post.id == post_id, Post.user_id == user_id).first()

            if not post_for_update:
                 raise Exception('Post not found')

            if title:
                post_for_update.title = title

            if description:
                post_for_update.description = description

            db.commit()
            db.refresh(post_for_update)
            return UpdatePostNode(post_for_update=post_for_update)

class DeletePostNode(SQLAlchemyObjectType):
    success = Field(lambda: String)

    class Arguments:
        id = ID(required=True)

    def mutate(self, info, post_id):
        db = get_db()

        post = db.query(Post).filter(Post.id == post_id).first()

        if not post:
            raise Exception('Post not found')

        db.delete(post)
        db.commit()
        return DeletePostNode(success=f'Post with id {post_id} deleted successfully')