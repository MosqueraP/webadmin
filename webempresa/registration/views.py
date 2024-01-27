from registration.forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth.forms import UserCreationForm # formulario generico
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from registration.models import Profile

# Create your views here.

# vista de registro ususarios
class SignUpView(CreateView):
    # form_class = UserCreationForm # quitamos el formulario generico
    form_class = UserCreationFormWithEmail # formulario extencion desde registration.form.py
    template_name = 'registration/signup.html' #carag el template en esta ubicación

    def get_success_url(self):
        return reverse_lazy('login') + '?register' # redireccionar a login a login
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # modificar en tiempo real los widges
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder':'Nombre de ususario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder':'Direccion email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Repite la contraseña'})
        # form.fields['username'].label = '' #quita las label
        return form
    
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # recuperar el objeto que se va editar
    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
# vista para editar el email dentro del perfil
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile') # al editar volver al perfil
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar        
        return self.request.user

    def get_form(self, form_clas=None):
        # widge email
        form = super(EmailUpdate, self).get_form()
        # modificar en tiempo real los widges
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder':'Email'})
        return form