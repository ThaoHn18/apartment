
from django.urls import path,include
from .views.users import RegisterView, LoginAPIView, LogoutAPIView, Change_passwordAPIview
from .views.role import RoleViewSet


from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("role", views.RoleViewSet, "role")
router.register("permisssion", views.PermissionsViewSet, "permisssion")


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('change-password/', Change_passwordAPIview.as_view(), name='change-password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
