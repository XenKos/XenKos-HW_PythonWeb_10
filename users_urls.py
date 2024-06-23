from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),  # змінено з views.signup на views.signupuser
]