# Generated by Django 4.2.2 on 2023-10-20 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("title", models.CharField(blank=True, max_length=300)),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(default="image.webp", upload_to="")),
                ("demo_link", models.CharField(blank=True, max_length=400, null=True)),
                (
                    "source_link",
                    models.CharField(blank=True, max_length=400, null=True),
                ),
                ("vote_count", models.IntegerField(default=0)),
                ("vote_ratio", models.IntegerField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("body", models.TextField(default="")),
                (
                    "value",
                    models.CharField(
                        choices=[("+", "Ijobiy"), ("-", "Salbiy")], max_length=50
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_review",
                        to="project.project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.profil",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="tag",
            field=models.ManyToManyField(
                blank=True, related_name="project_tag", to="project.tag"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.profil",
            ),
        ),
    ]
