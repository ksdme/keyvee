from rest_framework import viewsets
from api.models import Blob
from api.serializers import BlobSerializer


class BlobViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for the managing the blobs on a namespace.
    """

    authentication_classes = tuple()
    permission_classes = tuple()

    lookup_field = "key"
    queryset = Blob.objects.all()
    serializer_class = BlobSerializer

    @property
    def namespace(self):
        return self.kwargs["namespace"]

    def get_queryset(self):
        return self.queryset.filter(namespace=self.namespace)

    def get_serializer_context(self):
        return {
            **super().get_serializer_context(),
            "namespace": self.namespace,
        }
