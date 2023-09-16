from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutUs, name='about'),
    path('add-link/', views.AddLinkView.as_view(), name='add-link'),
    path('link/<slug>', views.FollowLink, name='follow-link')
]
