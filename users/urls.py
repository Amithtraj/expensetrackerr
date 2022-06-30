from django.urls import path
from .views import Record, Login, Logout
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'users'
router = DefaultRouter()
router.register(r"user", views.ListUserViewSet)

urlpatterns = [
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path("", include(router.urls)),
]
