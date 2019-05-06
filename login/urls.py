from django.urls import path
from .views import *
from .register import register

urlpatterns = [
    # path('login')
    path('user', register.register_user)

]
