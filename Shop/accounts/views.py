from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import obtain_auth_token

login = obtain_auth_token


class Register(CreateAPIView):
    def get(self, request):
        return Response({"hello"})
    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response({"message": "user create successfully"}, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "user logout"}, status=status.HTTP_204_NO_CONTENT)







