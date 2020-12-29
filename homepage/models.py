from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    working_organization = models.CharField(
        max_length=60, default="working_organization")
    domain = models.CharField(max_length=50, default="domain")
    designation = models.CharField(max_length=50, default="designation")
    skill_sets = models.CharField(max_length=50, default="skillsets")

    email = models.EmailField(max_length=150, unique=True)

    username = models.CharField(max_length=20, unique=True, default="username")

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    phone = models.CharField(max_length=20)

    gender = models.CharField(max_length=10)
