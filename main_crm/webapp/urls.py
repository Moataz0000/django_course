from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('my-login/', views.my_login, name='login'),
    path('dashbaord/', views.dashboard, name='dashboard'),
    path('logout/', views.my_logout, name='logout'),

    path('create-record/', views.create_record, name='createrecord'),
    path('view/<int:record_id>/', views.view_record, name='view_recorde'),
    path('update/<int:record_id>/', views.update_record, name='update_record'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('search/', views.search, name='search'),


]