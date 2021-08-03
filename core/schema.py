import blog.schema
import graphene


class Query(blog.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
