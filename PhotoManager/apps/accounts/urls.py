from django.urls import path
from .views import RegisterAdminView

urlpatterns = [
    path('register-admin/', RegisterAdminView.as_view(), name='register-admin'),
]
