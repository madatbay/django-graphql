import graphene
from graphene import ObjectType, relay
from graphene.types import interface
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from blog.models import Article, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'articles')

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ('id', 'name', 'body', 'category')


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

class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)
            
schema = graphene.Schema(query=Query)
