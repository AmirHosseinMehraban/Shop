from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .manager import MyUserManager



class MyUser(AbstractBaseUser):
    email = models.EmailField( max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email", "full_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otpcode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code}'

class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    verificationCode = models.CharField(max_length=4)
    isVerification = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


