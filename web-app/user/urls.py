from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from user import views as user_view



urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name = 'user/login.html'), name='login'),
#    path('login/', auth_view.LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name = 'success'),
#    path('search/', views.search, name = 'search'),
#    path('', views.main, name = 'main'),
    path('ridecreate/', views.rideCreation, name='rideCreation'),
    path('driverRegister/', views.driverRegister, name='driverRegister'),
    path('userMain/', views.userMain, name='userMain'),
    path('driverMain/', views.driverMain, name='driverMain'),
    path('userUpdate/', views.userUpdate, name='userUpdate'),
    path('share_success/<int:passengerNum>/<int:ride_id>', views.share_success, name='share_success'),
    path('confirm_success/<int:ride_id>', views.confirm_success, name='confirm_success'),
    path('complete_success/<int:ride_id>', views.complete_success, name='complete_success'),
    path('driverUpdate/', views.driverUpdate, name='driverUpdate'),
    path('searchShareableRide/', views.searchShareableRide, name='searchShareableRide'),
    path('searchUnconfirmedRide/', views.searchUnconfirmedRide, name='searchUnconfirmedRide'),
    path('<int:user_id>/startTimeEdit/<int:ride_id>', views.startTimeEdit, name = 'startTimeEdit'),
    path('<int:user_id>/areaEdit/<int:ride_id>', views.areaEdit, name = 'areaEdit'),
    path('<int:user_id>/destinationEdit/<int:ride_id>', views.destinationEdit, name = 'destinationEdit'),
    path('<int:user_id>/passengerNumEdit/<int:ride_id>', views.passengerNumEdit, name = 'passengerNumEdit'),
    path('<int:user_id>/shareableEdit/<int:ride_id>', views.shareableEdit, name = 'shareableEdit'),
]