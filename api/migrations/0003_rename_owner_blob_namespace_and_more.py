# Generated by Django 4.1.1 on 2022-09-27 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_blob_created_blob_updated"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blob",
            old_name="owner",
            new_name="namespace",
        ),
        migrations.AlterUniqueTogether(
            name="blob",
            unique_together={("namespace", "key")},
        ),
    ]
