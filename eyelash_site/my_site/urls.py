from django.urls import path
from .views import *

urlpatterns = [
    path('', RenderHomeView.as_view(), name='home'),
]
