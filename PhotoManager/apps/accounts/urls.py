# apps/accounts/urls.py
from django.urls import path
from .views import RegisterAdminView, InviteUserView, RegisterWithInviteView

urlpatterns = [
    path('register-admin/', RegisterAdminView.as_view(), name='register-admin'),
    path('invite/', InviteUserView.as_view(), name='invite-user'),
    path('register-with-invite/', RegisterWithInviteView.as_view(), name='register-with-invite'),
]