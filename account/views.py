from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = "account/register.html"


class EditProfileView(UpdateView):
    fields = ['first_name', 'last_name']
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
