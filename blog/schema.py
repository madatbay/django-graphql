import graphene
from graphene_django import DjangoObjectType, fields

from blog.models import Article, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'articles')

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ('id', 'name', 'body', 'category')

class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticleType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_articles(root, info):
        return Article.objects.select_related('category').all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
            
schema = graphene.Schema(query=Query)
