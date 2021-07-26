from django.http.response import HttpResponse

def index(request):
    return HttpResponse('To use GraphQL go to /graphql')