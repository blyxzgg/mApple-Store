from django.urls import path
from .views import main_page, login_page, register_page, logout_func, profile_page

app_name = 'main'

urlpatterns = [
    path('', main_page, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_func, name='logout'),
    path('profile/', profile_page, name='profile')
]
