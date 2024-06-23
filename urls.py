from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
# URL-маршрути для скидання паролю
    path('accounts/', include('django.contrib.auth.urls')),  
    path('reset_password/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


