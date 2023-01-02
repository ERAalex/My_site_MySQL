from django.urls import path
from . import views



urlpatterns = [

########################### RUS PART ###########################
    path('', views.index, name='index'),
    path('maria_project', views.maria_project, name='maria_project'),
    path('projects', views.projects, name='projects'),


########################### ENG PART ###########################
    path('eng_version', views.eng_index, name='eng_index'),


########################### ESP PART ###########################
    path('esp_version', views.esp_index, name='esp_index'),

]
