from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import CustomUserForm
# Create your views here.
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import CustomUser
from profiles.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password


class UserRegistration(CreateView):
    template_name = 'register.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        user.password = make_password(
            form.cleaned_data['password']
        )
        Profile.objects.create(user=user)
        return super().form_valid(form)
    


class UserLogin(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    model = CustomUser

    def get_success_url(self) -> str:
        if self.request.user.is_authenticated:
            profile_id = Profile.objects.get(user=self.request.user)
            return reverse('profile', kwargs={'pk': profile_id.pk})
        else:
            return redirect('login')

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
            profile = Profile.objects.get(user=user)
            print(profile.pk)
            # return reverse_lazy('profile', kwargs={'pk': profile_id.pk})
            return redirect(reverse('profile', kwargs={'pk': profile.pk}))

    return render(
        request=request,
        template_name='login.html',
        context=context
    )

def logout_view(request):
    logout(request=request)
    return redirect('login')
