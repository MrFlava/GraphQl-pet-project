import graphene

#TODO:
# 2. Create schemas;
# 3. Create auth;
# 4. Create CRUD endpoints for Post model
# 5. Create Readme.md


class Query(graphene.ObjectType):
  hello = graphene.String(name=graphene.String(default_value="World"))

  def resolve_hello(self, info, name):
    return 'Hello ' + name


schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello'])
