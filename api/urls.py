from rest_framework import routers
from api.views import BlobViewSet


router = routers.SimpleRouter()

# FIXME: Empty router prefix is not a good idea.
router.register(r"", BlobViewSet)

urlpatterns = router.urls
