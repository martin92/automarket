from django.conf.urls.defaults import patterns, url
from demo2.apps.home.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('demo2.apps.home.views',
	#URL DE LA VISTA INDEX
	url(r'^$',index_view, name = 'vista_principal'),

	#URL DE LA VISTA ABOUT
	url(r'^about/$',about_view, name = 'vista_about'),

	#URL DE LA VISTA DE CONTACTO
	url(r'^contacto/$', contacto_view, name = 'vista_contacto'),

	#URL DE LA VISTA LOGIN
	url(r'^login/$', login_view, name = 'vista_login'),

	#URL DE LOGOUT
	url(r'^logout/$',logout_view, name = 'vista_logout'),

	#URL DE LA VISTA SIGNUP
	url(r'^signup/$', register_view, name = 'vista_register'),

	#URL DE LA VISTA REGISTRAR AUTOS
	url(r'^registrar/auto/$', autos_view, name = 'vista_autos'),

	#URL DE LA VISTA REGISTRAR AUTOS
	#url(r'^registrar/anuncio/$', anuncios_view, name = 'vista_NUsuario'),

	url(r'^perfil/usuario/(?P<username>\d+)/$', perfil_view,name='vista_perfil'),

	url(r'^anuncios/numero/(?P<Id_anuncio>\d+)/$', anuncio_view,name='vista_anuncio'),
	#URL DE LA VISTA CREAR PERFIL
	url(r'^perfil/crear/$', usuarios_view,name='vista_crearp'),
	url(r'^perfil/ver/$', verperfil_view,name='vista_verp'),

	url(r'^visto/numero/(?P<Id_anuncio>\d+)/$', vistos_view, name='vista_vistos'),
	url(r'^reportado/numero/(?P<Id_anuncio>\d+)/$', reportado_view, name='vista_reportado'),
	url(r'^eliminar/auto/(?P<Id_anuncio>\d+)/$', eliminarauto_view,name='vista_eliminarauto'),
	
	url(r'^ver/anuncios/$', misanuncios_view,name='vista_misanuncios'),
	url(r'^calificar/$', calificar_view, name = 'vista_calificar'),
	url(r'^calificacion/$', vercalificacion_view, name = 'vista_vercalificacion'),

	#URL DE LAS BUSQUEDAS
	url(r'^buscar/marca/$', bmarca_view,name='vista_bmarca'),

	url(r'^buscar/year/$', bYear_view,name='vista_byear'),

	url(r'^buscar/precio/$', bprecio_view,name='vista_bprecio'),

	url(r'^buscar/ubicacion/$', bubicacion_view,name='vista_bubicacion'),

	url(r'^ordenar/marca/$', ordenmarca_view,name='vista_omarca'),

	url(r'^ordenar/year/$', ordenyear_view,name='vista_oyear'),

	url(r'^ordenar/precio/$', ordenprecio_view,name='vista_oprecio'),

	url(r'^ordenar/ubicacion/$', ordenubicacion_view,name='vista_oubicacion'),

)


