from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm
from .models import User
from .tokens import email_verification_token
from .utils import send_verification_email
from django.views import View
from django.shortcuts import render
from .models import SplashBanner
class SplashView(View):
    def get(self, request):
        return render(request, 'accounts/splash.html')
class SplashView(View):
    def get(self, request):
        banner = SplashBanner.objects.first()
        return render(request, 'accounts/splash.html', {
            'banner': banner
        })

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # inactive user
            send_verification_email(user, request)
            return HttpResponse(
                "Account created! Please check your email to confirm your account."
            )
        return render(request, 'accounts/signup.html', {'form': form})
class VerifyEmailView(View):
    def get(self, request, uid, token):
        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            return HttpResponse("Invalid verification link")

        if email_verification_token.check_token(user, token):
            user.is_active = True
            user.is_email_verified = True
            user.save()
            return HttpResponse("Email verified successfully! You can login now.")
        else:
            return HttpResponse("Verification link expired or invalid.")
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_email_verified:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Please verify your email before login.")
        else:
            messages.error(request, "Invalid email or password")

        return render(request, 'accounts/login.html')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
