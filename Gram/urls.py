from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit/', views.profile_edit, name='edit'),
    url(r'^post/', views.post, name='post'),
    url(r'^comment/', views.comment, name='comment'),
    url(r'^all/', views.all, name='all'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
