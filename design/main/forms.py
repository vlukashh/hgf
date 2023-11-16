from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms
from .models import AdvUser








class RegisterUserForm(forms.ModelForm):

   email = forms.EmailField(required=True,
                            label='Адрес электронной почты')
   password1 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
   password2 = forms.CharField(label='Пароль (повторно)',
                               widget=forms.PasswordInput,
                               help_text='Повторите тот же самый пароль еще раз')
   agree_to_processing = forms.BooleanField(required=True,
                                            widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


   def clean_password1(self):
       password1 = self.cleaned_data['password1']
       if password1:
           password_validation.validate_password(password1)
       return password1


#проверка на совпадения двух паролей
   def clean(self):
       super().clean()
       password1 = self.cleaned_data['password1']
       password2 = self.cleaned_data['password2']
       if password1 and password2 and password1 != password2:
           errors = {'password2': ValidationError(
               'Введенные пароли не совпадают', code='password_mismatch'
           )}
           raise ValidationError(errors)


   def save(self, commit=True):
       user = super().save(commit=False)
       user.set_password(self.cleaned_data['password1'])
       user.is_active = False
       user.is_activated = False
       if commit:
           user.save()
       return user


   class Meta:
       model = AdvUser
       fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'agree_to_processing')