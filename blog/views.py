from django.http.response import HttpResponse

def index(request):
    return HttpResponse('<h1>To use GraphQL go to <a href="/graphql">/graphql</a></h1>')