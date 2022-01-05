
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views

import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('logout/', authentication.views.logout_page, name='logout'),
    path('flux/',  blog.views.flux_page, name='flux'),
    path('create_ticket/', blog.views.create_ticket, name='create_ticket'),
    path('post/', blog.views.post_page, name='post'),
    path('subscription/', blog.views.subscript_page, name='subscrip'),
    path('review/', blog.views.create_review, name='review'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)