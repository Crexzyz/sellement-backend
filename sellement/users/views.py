from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.serializers import UserLoginSerializer
from users.serializers import UserModelSerializer

from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserLoginSerializer

        return UserModelSerializer

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        response = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(response, status=status.HTTP_201_CREATED)
