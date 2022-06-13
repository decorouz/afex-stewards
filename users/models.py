from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    about = models.TextField()
    birth_date = models.DateField(null=True)
    profile_photo = models.ImageField(
        null=True, upload_to="profiles", default="profiles/logo2.png", max_length=255
    )
    avatar_url = models.CharField(max_length=256, blank=True, null=True)
    social_google = models.CharField(max_length=250, null=True, blank=True)
    social_facebook = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

    @property
    def age(self):
        today = date.today()
        born = self.birth_date
        rest = 1 if (today.month, today.day) < (born.month, born.day) else 0
        return today.year - born.year - rest
