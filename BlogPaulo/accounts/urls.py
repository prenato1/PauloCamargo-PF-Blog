from django.urls import path
from .views import register, profile, profile_edit, CustomLoginView, CustomLogoutView, CustomPasswordChangeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile-edit'),
    path('password/', CustomPasswordChangeView.as_view(), name='password-change'),
]
