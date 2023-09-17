from django.urls import path
from .views import (RenderHomeView, ServiceDetailView, RecordingCreateView,
                    AuthorizationView, ExitAccountView, RegistrationView, PersonalAccountView)

urlpatterns = [

    path('', RenderHomeView.as_view(), name='home'),
    path('services/<int:id>/', ServiceDetailView.as_view(), name='service'),
    path('recording/', RecordingCreateView.as_view(), name='recording'),
    path('authorization/', AuthorizationView.as_view(), name='authorization'),
    path('exit_account/', ExitAccountView.as_view(), name='exit_account'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('personal_account/', PersonalAccountView.as_view(), name='personal_account'),

]
