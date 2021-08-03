import blog.schema
import graphene


class Query(blog.schema.Query, graphene.ObjectType):
    pass

class Mutation(blog.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
