from django.shortcuts import render
from rest_framework import generics, status, permissions
from .serializer import RegisrerSerializer, LoginSerializer, LogoutSerializer, ChangePasswordSerializer, GetUserReadOnlySerializer
from rest_framework.response import Response
from  rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.exceptions import APIException
from .mixins import GetSerializerClassMixin

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisrerSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"result": serializer.data,  "message": True }, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"result": serializer.data,  "message": True }, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Message": "Logout Succsesful"}, status=status.HTTP_204_NO_CONTENT)


class Change_passwordAPIview(generics.GenericAPIView, GetSerializerClassMixin):

    serializer_class = ChangePasswordSerializer

    permission_classes =[permissions.IsAuthenticated]

    serializer_action_classes = {
        # "list": UserReadOnlySerializer,
        # "retrieve": UserReadOnlySerializer,
    }

    # permission_classes_by_action = {
    #     'list': [IsAdminUser],
    #     "post": [IsAuthenticated],
    #     "update_status_meeting": [AllowAny],
    # }

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.validated_data["old_password"]):
            raise APIException(_("Old password is wrong."))
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        serializer = GetUserReadOnlySerializer(user)
        return Response({"result": serializer.data,  "message": True }, status=status.HTTP_200_OK)



    # def get_permissions(self):
    #     try:
    #         # return permission_classes depending on `action`
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except KeyError:
    #         # action is not set return default permission_classes
    #         return [permission() for permission in self.permission_classes]