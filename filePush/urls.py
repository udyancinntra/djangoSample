from django.urls import path,include
from .views import filePush

urlpatterns = [
    path('push/',filePush)
]