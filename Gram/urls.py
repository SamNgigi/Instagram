from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit/', views.profile_edit, name='edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
