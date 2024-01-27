from django import forms
from django.contrib.auth.forms import UserCreationForm # formulario generico
from django.contrib.auth.models import User
from registration.models import Profile


# Extender el formulario generico para que tenga correo y recuperar contraseñas
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo y debe ser valido.')

    class Meta:
        # nuevo campo de emeail en el fomulario
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # validacion si email existe para no duplicidad
    def clean_email(self):
            email= self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya está registrado, prueba con otro')
            return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3', 'placeholder': 'Avatar'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enlace'}), 
        }

# formulario para editar el email dentro del perfil
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo y debe ser valido.')
    class Meta:
        model = User
        fields = ['email'] # campo a editar
        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control-file mt-3'}),
        #     }    

    def clean_email(self): # validacion que el email sea unico
            email= self.cleaned_data.get("email")
            if 'email' in self.changed_data: # verificar si este email se encuentra en la data
                if User.objects.filter(email=email).exists():
                    raise forms.ValidationError('El email ya está registrado, prueba con otro')
            return email