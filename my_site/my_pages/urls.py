from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('/maria_project', views.maria_project, name='maria_project'),
    path('/projects', views.projects, name='projects')
    # path('test', views.test, name='test_test'),

]
