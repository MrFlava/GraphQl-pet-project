import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from core import Mutation, Query

#TODO:
# 3. Create auth;
# 4. Create CRUD endpoints for Post model
# 5. Create Readme.md

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def ping():
    return {"ping": "pong"}