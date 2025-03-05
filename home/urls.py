from django.urls import path
from home import views
urlpatterns = [
    path('register/',views.RegisterAPI.as_view()),
]
