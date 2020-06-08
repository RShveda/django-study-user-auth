from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    website = models.URLField(max_length = 80)
    profile_image = models.ImageField(upload_to = "profile_images")

    def __str__(self):
        return self.user.username
