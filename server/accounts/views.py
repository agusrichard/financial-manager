from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.utils import IntegrityError
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AccountSerializer, AccountTokenObtainPairSerializer


class AccountTokenObtainPairView(TokenObtainPairView):
    serializer_class = AccountTokenObtainPairSerializer


@api_view(http_method_names=['POST'])
def register(request):
    try:
        serializer = AccountSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValueError('Please review your input again, make sure it is correct')
        serializer.save()
        return Response({'success': True, 'message': 'Success to register account'})
    except IntegrityError:
        return Response({'success': False, 'message': 'Please use a different email account'})
    except ValueError as e:
        return Response({'success': False, 'message': str(e)})

