import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    info = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    social_github = models.CharField(max_length=300, null=True, blank=True)
    social_youtube = models.CharField(max_length=300, null=True, blank=True)
    social_instagram = models.CharField(max_length=300, null=True, blank=True)
    social_telegram = models.CharField(max_length=300, null=True, blank=True)
    personal_website = models.CharField(max_length=300, null=True, blank=True)
    social_linkedin = models.CharField(max_length=300, null=True, blank=True)
    social_facebook = models.CharField(max_length=300, null=True, blank=True)
    social_leetcode = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to="profiles", default="profiles/default_profile.webp"
    )
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse("get_profile", args=[str(self.id)])


class Skill(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.name)
