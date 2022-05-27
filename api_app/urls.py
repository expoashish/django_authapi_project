from django.urls import path
from .views import *

urlpatterns = [
  path('', index, name="index"),
  path('addUser/', Record.as_view(), name="register"),
  path('login/', Login.as_view(), name="login"),
  path('logout/', Logout.as_view(), name="logout"),
]