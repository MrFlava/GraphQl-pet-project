from typing import List

from graphene import ObjectType, Field, String, ID, Int
from graphene_sqlalchemy import SQLAlchemyObjectType

from .db_utils import get_db
from .models import User, Post
