from django.urls import path
from .views import (RenderHomeView, ServiceDetailView, RecordingCreateView,
                    AuthorizationView)

urlpatterns = [
    path('', RenderHomeView.as_view(), name='home'),
    path('services/<int:id>/', ServiceDetailView.as_view(), name='service'),
    #path('schedules/<int:id>/', ScheduleListView.as_view(), name='schedule'),
    path('recording/', RecordingCreateView.as_view(), name='recording'),
    path('authorization/', AuthorizationView.as_view(), name='authorization'),
    # Запись на услугу
]
