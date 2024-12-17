from django.urls import path
from . import views
urlpatterns = [
    path('sreg',views.sreg,name="sreg"),
    path('slog',views.slog,name="slog"),
    path('shome',views.shome,name='shome'),
    path('seditprofile', views.seditprofile,name='seditprofile'),
    # path('searchs', views.searchs,name='searchs'),
]