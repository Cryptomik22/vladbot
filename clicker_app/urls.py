from django.urls import path
from . import views

urlpatterns = [
    path('', views.click_counter, name='click_counter'),
    path('click/', views.increment_click, name='increment_click'),
    path('reset/', views.reset_clicks, name='reset_clicks'),
    path('decrement/', views.decrement_clicks, name='decrement_clicks')

]