from django.conf.urls import include, url
import views 

urlpatterns = [
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^profile$', views.profile, name='profile'),
]