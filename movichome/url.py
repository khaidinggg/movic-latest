from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'search'
#app_name = 'about'
#app_name = 'feedback'
urlpatterns = [
    url(r'^$', views.result, name='result')
   # url(r'^$, views.about, name='about' )
   # url(r'^$, views.feedback, name='feedback' )
    # path('', views.index, name='index')
    ]

