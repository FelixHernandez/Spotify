from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#Formulario para crear Usuarios con email
class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model=User
		fields=('username','email')

	#def clean_email(self):


class EmailAuthForm(forms.Form):
	email =forms.EmailField()
	password=forms.CharField(label='Password: ',widget=forms.PasswordInput)

	def __init__(self,*args,**kwargs):
		self.user_cache=None
		#Herencia Padre
		super(EmailAuthForm,self).__init__(*args,**kwargs)

	def clean(self):
		email=self.cleaned_data.get('email')
		password=self.cleaned_data.get('password')

		self.user_cache= authenticate(email=email, password=password)

		#validacion del usuario y el password para dar o denegar el acceso
		if self.user_cache is None:
			raise forms.ValidationError('Usuario Incorrecto')
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario Inactivo')
		return self.cleaned_data

	def get_user(self):
		return self.user_cache