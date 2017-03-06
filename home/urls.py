from django.conf.urls import url
from . import views

app_name = "home"

urlpatterns = [

    #/home/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/home/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

