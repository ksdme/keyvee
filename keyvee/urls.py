"""keyvee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="KeyVee API",
      default_version='v1',
      description=(
        "KeyVee is a namespaced key value store. This API does not require "
        "any authentication. All data and operations you generate and consume "
        "will happen under a namespace. Therefore, to use this API you have to "
        "generate a random UUID4 namespace for yourself."
      ),
   ),
   public=True,
   authentication_classes=[],
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # FIXME: Ugly hack to get the namespaced prefix in the url to work.
    # This uuid prefix should be moved to the api router.
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("<uuid:namespace>/", include("api.urls")),
    path("admin/", admin.site.urls),
]
