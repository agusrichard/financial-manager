from rest_framework import status
from rest_framework import exceptions
from django.db.utils import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
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
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=['POST'])
def login(request):
    try:
        serializer = AccountSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValueError(_('Invalid data. Please try again!'))

        email = request.data.get('email', None)
        password = request.data.get('password', None)
        credentials = {
            get_user_model().USERNAME_FIELD: email,
            'password': password
        }
        user = authenticate(**credentials)
        print('user', user)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Wrong email or password'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('Inactive user'))

        refresh = RefreshToken.for_user(user)

        serializer = AccountSerializer(user)
        user_data = serializer.data.copy()
        user_data.pop('password', None)

        return Response({
            'success': True,
            'message': 'Success to login',
            'token': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            },
            'user': user_data
        })
    except ValueError as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except exceptions.AuthenticationFailed as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

