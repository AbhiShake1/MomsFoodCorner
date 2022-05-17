from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login_user),
    path('get_user/username=<str:username>', views.get_user),
]