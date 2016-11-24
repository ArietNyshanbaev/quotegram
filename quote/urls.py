from django.conf.urls import include, url
import views 

urlpatterns = [
    url(r'^create_quote$', views.create_quote, name='create_quote'),
    url(r'^edit_quote/(?P<quote_id>.+)$', views.edit_quote, name='edit_quote'),
    url(r'^delete_quote/(?P<quote_id>.+)$', views.delete_quote, name='delete_quote'),
]