from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserForm
# Create your views here.
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import CustomUser
from profiles.models import Profile
from django.contrib.auth import authenticate, login, logout


class UserRegistration(CreateView):
    template_name = 'register.html'
    form_class = CustomUserForm
    success_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        Profile.objects.create(user=user)
        return super().form_valid(form)
    


# class UserLogin(LoginView):
#     template_name = 'login.html'
#     redirect_authenticated_user = True
#     # form_class = CustomUserForm
#     # model = CustomUser

#     # success_url = reverse_lazy('profile')
#     def form_valid(self, form: AuthenticationForm) -> HttpResponse:
#         print(form.cleaned_data)
#         return super().form_valid(form)

#     def get_success_url(self) -> str:
#         print(self.request.user)
#         profile_id = Profile.objects.get(user=self.request.user)
#         return reverse_lazy('profile', kwargs={'pk': profile_id})
    
def login_view(request):
    context = {}
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            request=request,
            username=email, 
            password=password
        )
        print(user)
        if user is not None:
            print('yeah')
            login(request, user)
            profile_id = Profile.objects.get(user=user)
            return reverse_lazy('profile', kwargs={'pk': profile_id})

    return render(
        request=request,
        template_name='login.html',
        context=context
    )
