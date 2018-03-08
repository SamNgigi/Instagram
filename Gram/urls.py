from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit/', views.update_profile, name='edit'),
    url(r'^post/', views.post, name='post'),
    url(r'^comment/(?P<pk>\d+)', views.comment, name='comment'),
    url(r'^all/', views.all, name='all'),
    url(r'^search/', views.search_result, name='search'),
    url(r'^ajax/likes/(?P<pk>\d+)', views.likes, name='likes'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
