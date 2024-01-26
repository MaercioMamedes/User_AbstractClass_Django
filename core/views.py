from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .models import MyUser
from .forms import CreateUserForm


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUserView(FormView):
    form_class = CreateUserForm
    model = MyUser
    template_name = "create_user.html"
