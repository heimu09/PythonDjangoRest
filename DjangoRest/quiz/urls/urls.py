from django.contrib import admin
from django.urls import path, include
from settings.base import ADMIN_URL


urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path('user/', include('auths.urls')),
    path('quiz/', include('ask.urls')),
]
