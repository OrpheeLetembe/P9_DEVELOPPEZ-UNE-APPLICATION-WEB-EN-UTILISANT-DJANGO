
from django.contrib import admin
from django.urls import path

import authentication.views

import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('create_ticket/', blog.views.create_ticket, name='create_ticket'),
]