# -*- encoding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from demo2.apps.home.forms import *
from demo2.apps.home.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.db.models import Q


#VISTA DE INICIO
def index_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		lista_carros = Autos.objects.all().order_by('-Id_anuncio')
		ctx = {'datos':datos,'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))
	else:
		lista_carros = Autos.objects.all().order_by('-Id_anuncio')
		ctx = {'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))

#VISTA DE PERFIL
def perfil_view(request, userprofile_id = 1):
	perfil = UserProfile.objects.get(id = userprofile_id)
	datos = UserProfile.objects.filter(user = request.user)
	ctx = {'perfil':perfil,'datos':datos}
	return render_to_response('home/perfil.html',ctx)


#VISTA DE ABOUT
def about_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		ctx = {'datos':datos}
		return render_to_response('home/about.html',ctx,context_instance = RequestContext(request))
	else:
		return render_to_response('home/about.html',context_instance = RequestContext(request))	


#VISTA DE CONTACTO
def contacto_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		formulario = ContactoForm()
		ctx = {'form':formulario,'datos':datos}
		return render_to_response('home/contacto.html',ctx, context_instance = RequestContext(request))
	else:
		formulario = ContactoForm()
		ctx = {'form':formulario}
		return render_to_response('home/contacto.html',ctx, context_instance = RequestContext(request))


# VISTA DE INSERCION DE PRODUCTOS
@login_required
def usuarios_view(request):
	if request.method == 'POST':
		form = UserProFileForm(request.POST,request.FILES)
		if form.is_valid():
			UserProfile = form.save(commit=False)
			UserProfile.user = request.user
			UserProfile = UserProfile.save()
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserProFileForm()
	ctx = {'form':form}
	return render_to_response('home/usuarios.html',ctx, context_instance = RequestContext(request))


#VISTA DE INSERCION DE PROVEEDORES
@login_required
def autos_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		if request.method == 'POST':
			form = AutosForm(request.POST, request.FILES)
			if form.is_valid():
				Autos = form.save(commit=False)
				Autos.Usuario = request.user
				Autos = Autos.save()
				form.save()
				return HttpResponseRedirect('/')
		else:
			form = AutosForm()
		ctx = {'form':form,'datos':datos}
		return render_to_response('home/autos.html',ctx, context_instance = RequestContext(request))
	else:
		if request.method == 'POST':
			form = AutosForm(request.POST, request.FILES)
			if form.is_valid():
				Autos = form.save(commit=False)
				Autos.Usuario = request.user
				Autos = Autos.save()
				form.save()
				return HttpResponseRedirect('/')
		else:
			form = AutosForm()
		ctx = {'form':form}
		return render_to_response('home/autos.html',ctx, context_instance = RequestContext(request))

def register_view(request):
	form = RegisterForm()
	if request.method =='POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=username,email=email,password=password_one)
			u.save()
			return HttpResponseRedirect('/login')
		else:
			ctx = {'form':form}
			return render_to_response('home/signup.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/signup.html',ctx,context_instance=RequestContext(request))


#VISTA DE LOGINS
def login_view(request):
	mensaje = ''
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			form = loginForm(request.POST)
			
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username = username,password = password)
				
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')

				else:
					mensaje = 'Usuario y/o password incorrectos!'
		
		
		form = loginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance = RequestContext(request))	



#VISTA DE LOGOUT
@login_required(login_url = '/login')
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


#----------------------------------------------------	BUSQUEDAS -------------------------------------------------------
#VISTA DE BUSQUEDA POR MARCA
def bmarca_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Marca =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/bmarca.html",{"results": results, "base": base, "datos": datos},context_instance = RequestContext(request))
	else:
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Marca =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/bmarca.html",{"results": results, "base": base},context_instance = RequestContext(request))


#VISTA DE BUSQUEDA POR AÑO
def bYear_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Year =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/byear.html",{"results": results, "base": base,"datos": datos},context_instance = RequestContext(request))
	else:
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Year =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/byear.html",{"results": results, "base": base},context_instance = RequestContext(request))


#VISTA DE BUSQUEDA POR PRECIO
def bprecio_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Precio =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/bprecio.html",{"results": results, "base": base, "datos": datos},context_instance = RequestContext(request))
	else:
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Precio =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/bprecio.html",{"results": results, "base": base},context_instance = RequestContext(request))

def bubicacion_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Ubicacion =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/bubicacion.html",{"results": results, "base": base, "datos": datos},context_instance = RequestContext(request))
	else:
		base =  request.GET.get('q', '')
		if base:
			qset = (
				Q(Ubicacion =  base)
				)
			results = Autos.objects.filter(qset)
		else:
			results = []
		return render_to_response("home/bubicacion.html",{"results": results, "base": base},context_instance = RequestContext(request))

def anuncio_view(request, Id_anuncio = 1):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		auto = Autos.objects.get(Id_anuncio = Id_anuncio)
		ctx = {'datos':datos,'auto':auto}
		return render(request, "home/anuncio.html",ctx)
	else:
		return render(request, "home/anuncio.html", {'auto': Autos.objects.get(Id_anuncio = Id_anuncio)})

def vistos_view(request, Id_anuncio):
	if Id_anuncio:
		a = Autos.objects.get(Id_anuncio = Id_anuncio)
		count = a.Visitas
		count += 1
		a.Visitas = count
		a.save()
	return HttpResponseRedirect('/')

def reportado_view(request,Id_anuncio):
	if Id_anuncio:
		a = Autos.objects.get(Id_anuncio = Id_anuncio)
		count = a.NumReportes
		count += 1
		count2 = a.Visitas
		count2 += 1
		a.NumReportes = count
		a.Visitas = count
		a.save()
		if a.NumReportes == 5:
			b = Autos.objects.get(Id_anuncio = Id_anuncio).delete()
			return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def eliminarauto_view(request,Id_anuncio):
	if Id_anuncio:
		a = Autos.objects.get(Id_anuncio = Id_anuncio)
		if a.Visitas >=0:
			b = Autos.objects.get(Id_anuncio = Id_anuncio).delete()
			return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

@login_required
def calificar_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		if request.method == 'POST':
			form = CalificacionForm(request.POST,request.FILES)
			if form.is_valid():
				Calificacion = form.save(commit=False)
				Calificacion.UsuarioCalificador = request.user
				Calificacion = Calificacion.save()
				form.save()
				return HttpResponseRedirect('/')
		else:
			form = CalificacionForm()
		ctx = {'form':form,'datos':datos}	
		return render_to_response('home/calificar.html',ctx, context_instance = RequestContext(request))
	else:
		if request.method == 'POST':
			form = CalificacionForm(request.POST,request.FILES)
			if form.is_valid():
				Calificacion = form.save(commit=False)
				Calificacion.UsuarioCalificador = request.user
				Calificacion = Calificacion.save()
				form.save()
				return HttpResponseRedirect('/')
		else:
			form = CalificacionForm()
		return render_to_response('home/calificar.html',{'form':form}, context_instance = RequestContext(request))
@login_required
def vercalificacion_view(request):
	datos = UserProfile.objects.filter(user = request.user)
	a = Calificacion.objects.filter(UsuarioCalificado = request.user)
	if request.user.is_active:
		b = Calificacion.objects.all()
		if b:
			datos = UserProfile.objects.filter(user = request.user)
			a = Calificacion.objects.filter(UsuarioCalificado = request.user)
	ctx = {'datos':datos,'a':a}
	return render_to_response('home/calificaciones.html',ctx,context_instance = RequestContext(request))

@login_required
def verperfil_view(request):
	return render_to_response('home/verperfil.html',{'datos':UserProfile.objects.get(user = request.user)} ,context_instance = RequestContext(request))

@login_required
def misanuncios_view(request):	
	if request.user.is_active:
		a = Autos.objects.filter(Usuario = request.user)
		ctx = {'a':a}
		return render_to_response('home/misanuncios.html',ctx,context_instance = RequestContext(request))

def ordenmarca_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		lista_carros = Autos.objects.all().order_by('Marca')
		ctx = {'datos':datos,'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))
	else:
		lista_carros = Autos.objects.all().order_by('Marca')
		ctx = {'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))

def ordenyear_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		lista_carros = Autos.objects.all().order_by('-Year')
		ctx = {'datos':datos,'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))
	else:
		lista_carros = Autos.objects.all().order_by('-Year')
		ctx = {'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))

def ordenprecio_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		lista_carros = Autos.objects.all().order_by('-Precio')
		ctx = {'datos':datos,'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))
	else:
		lista_carros = Autos.objects.all().order_by('-Precio')
		ctx = {'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))


def ordenubicacion_view(request):
	if request.user.is_active:
		datos = UserProfile.objects.filter(user = request.user)
		lista_carros = Autos.objects.all().order_by('Ubicacion')
		ctx = {'datos':datos,'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))
	else:
		lista_carros = Autos.objects.all().order_by('Ubicacion')
		ctx = {'lista_carros':lista_carros}
		return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))