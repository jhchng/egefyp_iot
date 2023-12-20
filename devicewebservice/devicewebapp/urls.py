from django.urls import path
from devicewebapp import views

#TEMPLATE URLS
app_name = 'devicewebapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    #path('hello/',views.hello, name='hello'),
]
