from django.urls import path

from .views import Home
from .views import BaseLoginView


app_name = 'public'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path(
        'login/',
        BaseLoginView.as_view(redirect_authenticated_user=True),
        name='login'
    )
]
