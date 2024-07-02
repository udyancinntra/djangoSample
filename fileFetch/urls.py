from django.urls import path,include
from .views import fileFetch

urlpatterns = [
    path('fetch/',fileFetch) ,
]