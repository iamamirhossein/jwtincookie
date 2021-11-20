from django.urls import path
from .views import LoginView

app_name = "jwt_cookie"

urlpatterns = [
    path('jwt/', LoginView.as_view(), name="login"),
]