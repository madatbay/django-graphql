from django.urls.conf import re_path
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from blog import schema

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^graphql/$', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
