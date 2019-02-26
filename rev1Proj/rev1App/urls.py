from django.urls import path

from . import views

# ROUTES TO LEAD TO LEAD TO VIEWS/FUNCTIONS
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/page2/<int:page2>/', views.page2, name='page2'),
    path('home/page3/<int:page3>/', views.page3, name='page3'),
    path('home/page4/<int:page4>/', views.page4, name='page4'),
    path('home/page5/<int:page5>/', views.page5, name='page5'),
    path('cocktails/', views.cocktails, name='cocktails'),
    path('cocktails/cocktails2/<int:drinkID>/', views.cocktails2, name='cocktails2'),


]