from django.urls import path,include
from .views import combination,home

urlpatterns = [
    path('',home,name='home'),
    #path('integer/<int:pk>',integer,name='integer'),
    #path('string/<str:pk>',integer,name='string'),
    #path('slug/<slug:pk>',integer,name='slug'),
    #path('path/<path:pk>',integer,name='path'),
    path('combination/<path:pk>/<str:id>/<slug:pkid>/<int:idpk>',combination,name="combination"),
    

]
