from django.urls import path
from .views import (
    SplashView,
    SignupView,
    VerifyEmailView,
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('', SplashView.as_view(), name='splash'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('verify-email/<int:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
