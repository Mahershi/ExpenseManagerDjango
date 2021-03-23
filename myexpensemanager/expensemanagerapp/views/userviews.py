from django.shortcuts import render
from rest_framework import viewsets
from ..models import User
from ..serializers import UserSerializer, ChangeUserPasswordSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_401_UNAUTHORIZED


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def partial_update(self, request: Request, *args, **kwargs):
        request.data.pop('password')
        print(str(request.data))
        super().partial_update

    def get_permissions(self):
        print(self.action)
        if self.action == 'create':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

    def list(self, request, *args, **kwargs):

        queryset = User.objects.all()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'success': 'true',
                'data': serializer.data
            }
        )

    def retrieve(self, request, *args, **kwargs):
        # do your customization here
        print(f' Args: {args}')
        print(f' Kwargs: {kwargs}')
        instance = self.get_object()
        print("instance: ")
        print(instance)
        serializer = self.get_serializer(instance)
        return Response(
            {
                "data": serializer.data,
                "success": "true"
            }
        )


class ChangeUserPasswordViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = ChangeUserPasswordSerializer



# custom auth token so that can return desired response
class ObtainAuthToken(ObtainAuthToken):

    def post(self, request):
        print(request)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(
                {
                    "success": "false",
                    "error": "Invalid Credentials",
                },
                status=HTTP_401_UNAUTHORIZED
            )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user = User.objects.get(id=token.user_id)

        # serializer = UserSerializer(user)
        return Response(
            {
                'success': 'true',
                'data': {
                    'auth_token': token.key,
                    'user': UserSerializer(user).data
                }
            }
        )


class CreateExistingToken(APIView):
    def get(self, request):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)

        return Response(
            {
                "success": "true"
            }
        )

class BaseTestView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response(
            {
                "success": "true",
                "msg": "Base Test - GET Success"
            }
        )

    def post(self, request):
        return Response(
            {
                "success": "true",
                "msg": "Base Test - POST Success"
            }
        )