from django.urls import path,include
from home import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('private/event',views.PrivateEventViewSet)


urlpatterns = [
    path('register/',views.RegisterAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),
    
    path('',include(router.urls)),
]
