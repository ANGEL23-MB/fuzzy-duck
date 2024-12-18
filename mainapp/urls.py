from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('reg',views.reg,name="reg"),
    path('log',views.log,name="log"),
    path('user',views.user,name='user'),
    path('editprofile', views.editprofile,name='editprofile'),
    path('searchs', views.searchs,name='searchs'),
    path('addrec', views.addrec,name='addrec'),
]