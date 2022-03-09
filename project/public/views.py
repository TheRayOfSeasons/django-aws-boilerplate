from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


class Home(TemplateView):
    """
    Renders the homepage.
    """

    template_name = 'public/home.jinja'


class BaseLoginView(LoginView):
    """
    Renders the custom login page
    """

    template_name = 'public/login.jinja'
