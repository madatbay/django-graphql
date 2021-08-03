import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from blog.models import Article, Category

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name','articles']
        interfaces = (relay.Node, )

class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'body': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class CategoryUpdateMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID()
        name = graphene.String(required=True)
        
    category = graphene.Field(CategoryNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, id):
        category = Category.objects.get(pk=from_global_id(id)[1])
        category.name = name
        category.save()

        return CategoryUpdateMutation(category=category)

class CategoryCreateMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        
    category = graphene.Field(CategoryNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        category = Category.objects.create(name=name)
        return CategoryCreateMutation(category=category)

class CategoryDeleteMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID()
        
    category = graphene.Field(CategoryNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        Category.objects.get(id=from_global_id(id)[1]).delete()
        return
class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)
class Mutation(graphene.ObjectType):
    create_category = CategoryCreateMutation.Field()
    update_category = CategoryUpdateMutation.Field()
    delete_category = CategoryDeleteMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
