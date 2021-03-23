from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, CreateExistingToken, ObtainAuthToken, ChangeUserPasswordViewSet, BaseTestView
from django.urls import path
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('change_password', ChangeUserPasswordViewSet)

urlpatterns = [
    path('tokens', CreateExistingToken.as_view(), name='gentoken_existing'),
    path('test', BaseTestView.as_view(), name="connection_test")
]
urlpatterns += router.urls
urlpatterns += [
    path('login', ObtainAuthToken.as_view())
]
