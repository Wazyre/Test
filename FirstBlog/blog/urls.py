from django.conf.urls import url
from blog import views
from blog.views import compiled_files, python, c, cplusplus, java


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name = 'home_page'),
    url(r'^about/$', views.AboutPageView.as_view(), name = 'about_page'),
    url(r'^python/$', python, name = 'python_files'),
    url(r'^c/$', c, name = 'c_files'),
    url(r'^c\+\+/$', cplusplus, name = 'c++_files'),
    url(r'^java/$', java, name = 'java_files'),
    #url(r'^file/$', views.FilePageView.as_view(), name = 'upload_file'),
    url(r'^compiled_files/$', compiled_files, name = 'compiled_files_page'),
    url(r'^compiled_files/compiled_files/$', compiled_files, name = 'compiled_files_page2'),
]
