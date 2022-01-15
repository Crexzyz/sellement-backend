from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth import logout as django_logout

from users.serializers import UserLoginSerializer
from users.serializers import UserModelSerializer

from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserLoginSerializer

        return UserModelSerializer

    @action(detail=False, methods=['POST'],
            permission_classes=[AllowAny])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        response = {}
        status_code = 0

        if not serializer.is_valid():
            response['error'] = 'Invalid credentials'
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            user, token = serializer.save()
            response['user'] = UserModelSerializer(user).data
            response['access_token'] = token
            status_code = status.HTTP_201_CREATED

        return Response(response, status=status_code)

    @action(detail=False, methods=['GET'])
    def logout(self, request):
        request.user.auth_token.delete()
        django_logout(request)

        return Response(status=status.HTTP_200_OK)
