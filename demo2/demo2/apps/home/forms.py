# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from demo2.apps.home.models import *
from django.contrib.auth.models import User

#forma de contacto
class ContactoForm (forms.Form):
	
	name = forms.CharField(widget = forms.TextInput())
	email = forms.EmailField(widget = forms.TextInput())
	comment = forms.CharField(widget = forms.Textarea())

#forma de productos
class AutosForm(ModelForm):
	class Meta:
		model = Autos
		exclude = ('Usuario', 'Visitas','NumReportes')

class ModificarAutoForm(ModelForm):
	class Meta:
		model = Autos
		fields = ('Precio','Comentarios')
#forma de proveedores
class UserProFileForm(ModelForm):
	class Meta:
		model = UserProfile
		exclude = 'user'

#Formulario de inicio de sesion
class loginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.PasswordInput(render_value = False))

class RegisterForm(forms.Form):
	username = forms.CharField(label = 'Nombre de Usuario',widget = forms.TextInput())
	email = forms.EmailField(label = 'Correo Electronico',widget = forms.TextInput())
	password_one = forms.CharField(label = 'Contrasena',widget = forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label = 'Confirmar Contrasena',widget = forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username = username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya registrado.')
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email = email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electronico ya registrado.')
	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no Coinciden')
#validar los campos de todos los modelos
class CalificacionForm(ModelForm):
	class Meta:
		model = Calificacion
		fields = ('UsuarioCalificado','Calificacion','Motivo')