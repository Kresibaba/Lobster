from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url('^$', login, {'template_name': 'lobster/login.html'}),
    url('^home.html$', views.home, name='home'),
    url('logout/$', logout, {'template_name':'lobster/logout.html'}),
    path('<int:projects_id>/', views.nonradData, name='nonradData'),
    re_path(r'^radData/$', views.radData, name='radData'),
]

