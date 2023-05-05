from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import ProfileForm
from .models import Profile


class ProfileList(ListView):
    template_name = 'profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context
    

class ProfileUpdate(UpdateView):
    template_name = 'profile_change.html'
    form_class = ProfileForm
    model = Profile
    # success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context
    