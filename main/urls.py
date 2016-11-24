from django.conf.urls import include, url
import views 

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^create_quote$', views.create_quote, name='create_quote'),
]