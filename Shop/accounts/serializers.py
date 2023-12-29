from rest_framework import serializers
from .models import MyUser, Otpcode, Profile




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
        user = MyUser.objects.create_user(phone_number=validated_data['phone_number'],
                                          email=validated_data['email'], full_name=validated_data['full_name'],
                                          password=validated_data['password'])
        return user

