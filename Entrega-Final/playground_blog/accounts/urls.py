from django.urls import path
from .views import profile_view, ProfileUpdateView, UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
