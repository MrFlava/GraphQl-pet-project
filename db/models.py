from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Post(Model):
    """Post Model"""


class User(Model):
    """User Model"""

    @has_many("id", "user_id")
    def posts(self):
        return Post