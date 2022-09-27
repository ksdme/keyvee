from rest_framework import serializers
from api.models import Blob


class BlobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blob
        fields = "__all__"
        read_only_fields = ("namespace",)

    def save(self, **kwargs):
        # Prevent the namespace from being changed once it is set.
        namespace = self.context["namespace"]
        return super().save(namespace=namespace, **kwargs)
