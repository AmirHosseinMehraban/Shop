from rest_framework import serializers
from .models import MyUser, Otpcode, Profile, Forgot
from django.utils import timezone





class OtpcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otpcode
        fields = ['phone_number', 'code']

    def create(self, validated_data):
        otp = Otpcode(phone_number=validated_data['phone_number'], code=validated_data['code'])
        otp.save()
        return otp


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = Profile
        fields = ['verificationCode', 'isVerification']

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=20)
    # profile = ProfileSerializer()

    class Meta:
        model = MyUser
        fields = ['phone_number', 'email', 'full_name', 'password', 'password2']


    def validate_password(self, data):
        password = data
        if len(password) < 8:
            raise serializers.ValidationError("password should be bigger than 8 char")
        return data

    def validate_email(self, data):
        email = data
        if MyUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("this email have")
        return data


    def validate_phone_number(self, data):
        phone_number = data
        if MyUser.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("this phone number have")
        return data

    def validate(self, data):
        password2 = data['password2']
        password = data['password']

        if password != password2:
            raise serializers.ValidationError("password should be the same")
        return data

    def create(self, validated_data):
        user = MyUser.objects.create_user(phone_number=validated_data['phone_number'], email=validated_data['email'],
                                          full_name=validated_data['full_name'],
                                          password=validated_data['password'])
        return user

class ForgotEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def validate_email(self, value):
        if MyUser.objects.filter(email=value).exists() and MyUser.objects.get(email=value).is_active:
            return value
        raise  serializers.ValidationError("there isent user with this email")

class VerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)
    verificationCode = serializers.CharField(max_length=4)

    # def validate_phone_number(self, value):
    #     if Profile.objects.filter(user=value).exists():
    #         print("@*99")
    #         return value
    #     raise serializers.ValidationError('phone number ... ')

    def validate_verificationCode(self, value):
        if len(value) != 4:
            raise serializers.ValidationError('verification code shoul be 4 character ... ')
        return value

class ForgotLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=4, min_length=4)
    password = serializers.CharField(max_length=100)
    password2 = serializers.CharField(max_length=100)

    def validate(self, data):
        email = data['email']
        code = data['code']
        password = data['password']
        password2= data['password2']

        if MyUser.objects.filter(email=email).exists() == False:
            raise serializers.ValidationError('email ...')
        if password !=password2:
            raise serializers.ValidationError('password should be match ... ')
        return data





