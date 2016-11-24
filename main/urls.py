from django.conf.urls import include, url
import views 

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^top_ten$', views.top_ten, name='top_ten'),
    url(r'^flop_ten$', views.flop_ten, name='flop_ten'),
    url(r'^last_quotes$', views.last_quotes, name='last_quotes'),
]