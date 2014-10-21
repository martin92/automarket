# -*- encoding: utf-8 -*-
from django.contrib import admin
from demo2.apps.home.models import *

class clientAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'creditos')
	list_filter = ('name',)
	search_fields = ('name',)

class empleadoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'puesto')
	list_filter = ('nombre',)
	search_fields = ('nombre',)



class userProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'photo', 'phone')
	list_filter = ('user',)
	search_fields = ('user',)




admin.site.register(Autos)
admin.site.register(UserProfile)
admin.site.register(Calificacion)
