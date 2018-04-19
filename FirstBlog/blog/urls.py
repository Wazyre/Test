from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^python/$', views.PythonPageView.as_view()),
    url(r'^c/$', views.CPageView.as_view()),
    url(r'^c\+\+/$', views.CPlusPlusPageView.as_view()),
]
