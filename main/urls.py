from django.conf.urls import include, url
import views 

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^create_quote$', views.create_quote, name='create_quote'),
    url(r'^edit_quote/(?P<quote_id>.+)$', views.edit_quote, name='edit_quote'),
]