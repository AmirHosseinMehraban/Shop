from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        if not phone_number:
            raise ValueError("Users must have a phone number")

        if not full_name:
            raise ValueError("Users must have a full name")

        user = self.model(
            phone_number=phone_number,
            full_name=full_name,
            email=self.normalize_email(email)

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, email, password=None):
        user = self.create_user(phone_number, full_name, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

