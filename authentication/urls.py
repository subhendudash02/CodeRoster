from django.contrib import admin
from django.urls import path, include
from . import views
from codechef import views as v1

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name='signout'),
    path('codechef-data',v1.display_data_codechef,name='codechef'),
    path('codeforces-data',v1.display_data_codeforces,name='codeforces'),
]
