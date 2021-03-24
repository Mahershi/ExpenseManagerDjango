from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, CreateExistingToken, ObtainAuthToken, ChangeUserPasswordViewSet, BaseTestView
from .views import ExpenseViewSet
from .views import ClusterViewSet, CategoryViewSet
from django.urls import path
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('change_password', ChangeUserPasswordViewSet)
router.register('expenses', ExpenseViewSet)
router.register('clusters', ClusterViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('tokens', CreateExistingToken.as_view(), name='gentoken_existing'),
    path('test', BaseTestView.as_view(), name="connection_test")
]
urlpatterns += router.urls
urlpatterns += [
    path('login', ObtainAuthToken.as_view())
]
