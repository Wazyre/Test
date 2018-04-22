from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name = 'home_page'),
    url(r'^about/$', views.AboutPageView.as_view(), name = 'about_page'),
    url(r'^python/$', views.PythonPageView.as_view(), name = 'python_files'),
    url(r'^c/$', views.CPageView.as_view(), name = 'c_files'),
    url(r'^c\+\+/$', views.CPlusPlusPageView.as_view(), name = 'c++_files'),
    url(r'^java/$', views.JavaPageView.as_view(), name = 'java_files'),
    url(r'^file/$', views.FilePageView.as_view(), name = 'upload_file'),
    url(r'^compiled_files/$', views.CompiledFilePageView.as_view(), name = 'compiled_files_page'),
]
