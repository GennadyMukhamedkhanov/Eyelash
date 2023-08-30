from django.urls import path
from .views import RenderHomeView, ServiceView, SheduleView, RecordingView

urlpatterns = [
    path('', RenderHomeView.as_view(), name='home'),
    path('service/', ServiceView.as_view(), name='service'),
    path('shedule/', SheduleView.as_view(), name='shedule'),  # Почему такой путь
    path('recording/', RecordingView.as_view(), name='recording'),  #Запись на услугу
]
