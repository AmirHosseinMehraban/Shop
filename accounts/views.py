from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer, ForgotEmailSerializer, VerifySerializer, ForgotLoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import obtain_auth_token
from .models import MyUser, Profile, Forgot
from rest_framework.permissions import AllowAny
from .utils import mail
import random
from django.utils import timezone

login = obtain_auth_token


class Register(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():

            user = MyUser.objects.create_user(phone_number=serializer.data['phone_number'],
                                              email=serializer.data['email'], full_name=serializer.data['full_name'],
                                              password=serializer.data['password'])
            user.is_active = False
            user.save()
            verification_code = str(random.randint(1000,9999))
            profile = Profile(user=user, verificationCode=verification_code)
            profile.save()
            mail(verification_code, user.email, user.full_name)
            return Response({"message": "send email please check it"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


class VerifyView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = VerifySerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['phone_number']

            verification_code = serializer.validated_data['verificationCode']

            profile = Profile.objects.filter(user__phone_number=username, verificationCode=verification_code)
            if profile.exists():
                if (timezone.now()- profile[0].created).total_seconds() > 120:
                    profile.delete()
                    user = MyUser.objects.get(phone_number=username)
                    user.delete()
                    return Response({"sign up again ... "})
                user = MyUser.objects.get(phone_number=username)
                user.is_active = True
                user.save()
                profile.delete()

                return Response({"user successfully added ...."})

        return Response(serializer.errors)


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "user logout"}, status=status.HTTP_204_NO_CONTENT)


class Test(APIView):
    def get(self, request):
        print("#" * 99)
        print(request.session['hello'])
        return Response({"hello"})


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = MyUser.objects.get(email=email)
            if user.is_active:
                code = str(random.randint(1000,9999))
                mail('1111', user.email, user.full_name)
                user_forgot=Forgot(user=user, code=code)
                user_forgot.save()
                return  Response({"message": "send you email please verify it"})
            return Response({"message": "this user is not verify code "})
        return Response(serializer.errors)

class ForgotLogin(APIView):
    def post(self, request):
        serializer = ForgotLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']
            password = serializer.validated_data['password']
            user = MyUser.objects.get(email=email)
            forgot_user = Forgot.objects.filter(user=user, code=code)
            if forgot_user.exists():
                forgot_user.delete()
                user.set_password(password)
                user.save()
                return Response({"message":"change password successfuly ... "})
            return Response({"message": "there is something ...."})
        return Response(serializer.errors)





