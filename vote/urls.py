from django.conf.urls import include, url
import views 

urlpatterns = [

    url(r'^vote/(?P<quote_id>.+)/(?P<type>.+)$', views.vote, name='vote'),
]