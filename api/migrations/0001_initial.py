# Generated by Django 4.1.1 on 2022-09-27 06:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("owner", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("key", models.CharField(db_index=True, max_length=128)),
                ("value", models.JSONField(blank=True, default=None, null=True)),
            ],
            options={
                "unique_together": {("owner", "key")},
            },
        ),
    ]
