from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import generic
from django.views.generic import TemplateView, DeleteView
from .forms import RegisterUserForm, CreateAppliForm
from django.core.signing import BadSignature
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LogoutView
from .models import AdvUser, Appli
from django.views.generic import CreateView



def index(request):
    num_applications = Appli.objects.filter(stas__exact='П').count()
    num_complete = Appli.objects.filter(stas__exact='В').order_by('-date')[:4]
    context = {
        'num_applications': num_applications,
        'num_complete': num_complete
    }
    return render(request, 'main/index.html', context)




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


class CreateAppliView(CreateView):
    form_class = CreateAppliForm
    template_name = 'main/create_appli.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAppliView, self).form_valid(form)

class AppliListView(generic.ListView):
    model = Appli
    context_object_name = 'application_list'
    template_name = 'application_list.html'

class DeleteAppliView(LoginRequiredMixin, DeleteView):
   model = Appli
   template_name = 'main/appli_delete.html'
   success_url = reverse_lazy('main:index')







