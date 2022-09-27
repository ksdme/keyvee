from django.contrib import admin
from api.models import Blob


@admin.register(Blob)
class BlobModelAdmin(admin.ModelAdmin):
    list_display = ("namespace", "key", "created", "updated")
