from django.urls import path
from .views import *

urlpatterns = [
    path('<str:time>', TimeStampView.as_view())
]
