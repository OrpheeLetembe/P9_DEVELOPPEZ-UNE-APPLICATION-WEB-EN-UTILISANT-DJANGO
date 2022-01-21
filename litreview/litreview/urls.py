
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views

import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='home'),
    path('Inscription/', authentication.views.signup_page, name='signup'),
    path('Déconnexion/', authentication.views.logout_page, name='logout'),
    path('flux/',  blog.views.flux_page, name='flux'),
    path("Création d'un ticket/", blog.views.create_ticket, name='create_ticket'),
    path('Post/', blog.views.post_page, name='post'),
    path('Abonnements/', blog.views.subscript_page, name='subscrip'),
    path("Création d'une critique/", blog.views.create_review, name='review'),
    path('Modifier ticket/<int:id>', blog.views.ticket_update, name='ticket_update'),
    path('Supprimer ticket/<int:id>', blog.views.ticket_delete, name='ticket_delete'),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
