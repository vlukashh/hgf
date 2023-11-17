from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .forms import RegisterUserForm
from django.core.signing import BadSignature
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import AdvUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView



def index(request):
   return render(request, 'main/index.html')




class BBLoginView(LoginView):
   template_name = 'main/login.html'




class RegisterUserView(CreateView):
   model = AdvUser
   template_name = 'main/register_user.html'
   form_class = RegisterUserForm
   success_url = reverse_lazy('main:register_done')



class RegisterDoneView(TemplateView):
   template_name = 'main/register_done.html'



def user_activate(request, sign):
   try:
       username = signer.unsign(sign)
   except BadSignature:
       return render(request, 'main/bad_signature.html')
   user = get_object_or_404(AdvUser, username=username)
   if user.is_activated:
       template = 'main/user_is_activated.html'
   else:
       template = 'main/activation_done.html'
       user.is_activated = True
       user.is_active = True
       user.save()
   return render(request, template)




@login_required
def profile(request):
   return render(request, 'main/profile.html')

class BBLogoutView(LoginRequiredMixin, LogoutView):
   template_name = 'main/logout.html'