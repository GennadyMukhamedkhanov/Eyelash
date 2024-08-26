

from django.urls import path

from api.views import (ServiceGetCreateView, ServiceSheduleGetView, BookingView,
                       PersonalListView, UserCreateView, TokenGetView,
                       SearchServiceView, CreatingServicesView)

urlpatterns = [
    path('users/', UserCreateView.as_view()),
    path('token/', TokenGetView.as_view()),

    path('service/', ServiceGetCreateView.as_view()),
    path('search_services/', SearchServiceView.as_view()),
    path('service/<int:pk>/shedule/', ServiceSheduleGetView.as_view()),
    path('booking/<int:pk>/', BookingView.as_view()),
    path('personal/<int:pk>/', PersonalListView.as_view()),

    path('creating_services/', CreatingServicesView.as_view()),


]