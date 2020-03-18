from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import *
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('blogs.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/login/', login_view, name='login'),

    path('accounts/register/', register_view, name='register'),

    path('accounts/logout/', logout_view,{ 'template_name': 'registration/logout.html',}, name='logout'),

    path('logged_out/', logged_out, name='logged_out'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)