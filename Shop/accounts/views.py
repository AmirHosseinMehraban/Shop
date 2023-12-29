from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import obtain_auth_token
from .models import MyUser, Profile
from rest_framework.permissions import AllowAny

login = obtain_auth_token


class Register(APIView):
    # CreateAPIView
    permission_classes = [AllowAny, ]
    def post(self, request):

        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = MyUser.objects.create_user(phone_number=serializer.data['phone_number'], email=serializer.data['email'],
                          full_name=serializer.data['full_name'], password=serializer.data['password'])
            user.is_active=False
            user.save()
            verification_code = '1234'
            profile = Profile(user=user, verificationCode=verification_code)
            profile.save()
            return Response({"message": "send email please check it"})
        return Response(serializer.errors)

class VerifyView(APIView):
    permission_classes = [AllowAny, ]
    def post(self, request):
        username = request.data.get('username', '')
        verification_code = request.data.get('verificationCode', '')
        print("#"*99)
        print(username)
        profile = Profile.objects.filter(user__phone_number=username, verificationCode=verification_code)
        if profile.exists():
            user = MyUser.objects.get(phone_number=username)
            user.is_active = True
            user.save()

        return Response({"user successfully "}, status=status.HTTP_200_OK)

class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "user logout"}, status=status.HTTP_204_NO_CONTENT)


class Test(APIView):
    def get(self, request):
        print("#"*99)
        print(request.session['hello'])
        return Response({"hello"})


class ForgotPasswordView(APIView):
    def post(self, request):
        ...









