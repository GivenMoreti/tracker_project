from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('complete/<int:id>/',views.delete,name='complete'),
    path('add_driver/',views.addDriver,name='add_driver'),
    path('delete_driver/<int:id>/',views.deleteDriver,name='delete_driver'),
    path('drivers/',views.driver,name='drivers'),
    path('add_job/',views.addJob,name='add_job'),
    path('update_tracker/<int:id>/',views.update,name='update_tracker'),
    path('update_driver/<int:id>/',views.updateDriver,name='update_driver'),
    path('chats/',views.chats,name='chats'),
    path('add_chat/',views.addChat,name='add_chat'),
    path('delete_chat/<int:id>/',views.deleteChat,name='delete_chat'),
    path('update_chat/<int:id>/',views.updateChat,name='update_chat'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path("register_user/", views.register, name="register_user"),
    path('job_history',views.history,name='job_history')

]
