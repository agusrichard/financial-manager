from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(http_method_names=['GET', 'POST'])
def create_account(request):
    return Response('Hello World!')
