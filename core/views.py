from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from .models import MyUser
from .forms import CreateUserForm


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateUserView(FormView):
    form_class = CreateUserForm
    template_name = "create_user.html"

    def post(self, request, *args, **kwargs):

        form = CreateUserForm(data=self.request.POST)
        if form.is_valid():

            return HttpResponse("é nois")
        else:
            return HttpResponse("deu ruim")
