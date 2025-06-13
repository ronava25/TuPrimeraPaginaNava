from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm, UserRegisterForm, CustomLoginForm


@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  
        return kwargs
    
    def form_valid(self, form):
        self.object = form.save(commit=True)
        messages.success(self.request, "Perfil actualizado correctamente.")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')