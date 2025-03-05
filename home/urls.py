from django.urls import path
from home import views
urlpatterns = [
    path('register/',views.RegisterAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),
]
