from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from django.shortcuts import redirect
from . forms import UserRegistrationForm, UserUpdateForm
# Create your views here.


class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'user_login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserAccountUpdateView(View):
    template_name = 'update_profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change.html', {'form': form})
