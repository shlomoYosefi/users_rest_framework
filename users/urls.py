from rest_framework.routers import DefaultRouter
from .views import UserViewSet ,loginViewSet
from django.urls import path,include



router = DefaultRouter()
router.register('user',UserViewSet)
router.register('login',loginViewSet,basename='login')


urlpatterns=[
    path('api/',include(router.urls))
]