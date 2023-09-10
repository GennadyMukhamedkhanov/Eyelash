from django.urls import path
from .views import (RenderHomeView, ServiceDetailView, ScheduleListView,
                    RecordingCreateView)

urlpatterns = [
    path('', RenderHomeView.as_view(), name='home'),
    path('services/<int:id>/', ServiceDetailView.as_view(), name='service'),
    path('schedules/<int:id>/', ScheduleListView.as_view(), name='schedule'),
    path('recording/<int:id>/', RecordingCreateView.as_view(),
         name='recording'),
    # Запись на услугу
]
