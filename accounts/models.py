from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
from django.db import models

class SplashBanner(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='splash/')

    def __str__(self):
        return self.title or "Splash Banner"
