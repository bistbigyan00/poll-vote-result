from django.urls import path
from poll import views

app_name = 'poll'

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create_poll,name='create'),
    path('vote/<str:pk>',views.vote,name='vote'),
    path('result/<str:pk>',views.result,name='result')
]
