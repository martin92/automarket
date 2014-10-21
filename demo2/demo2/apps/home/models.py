# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#from django_countries.fields import CountryField

# Create your models here.



#MODELO DE USUARIOS
'''class userProfile (models.Model):
	def url(self, filename):
		ruta = "MultimediaData/Users/%s/%s"% (self.User.username, filename)
		return ruta
	
	Usern = models.OneToOneField(User)
	Foto = models.ImageField(upload_to = url)
	Telefono = models.CharField(max_length = 15)
	Email = models.CharField(max_length = 20)
	Webpage = models.CharField(max_length = 20)
	Descripcion = models.TextField(max_length = 300)
	Direccion = models.CharField(max_length = 50)
	Nombre = models.CharField(max_length = 30)
	ApellidoP = models.CharField(max_length = 20)
	ApellidoM = models.CharField(max_length = 20)
	Puntos = models.IntegerField()
	#Pais = models.CountryField()
	Estado = models.CharField(max_length = 30)
	Ciudad = models.CharField(max_length = 30)
	
	def __unicode__(self):
		return self.Usern.username'''
class UserProfile(models.Model):
	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"% (self.user.username,filename)
		return ruta
	user = models.OneToOneField(User)
	Foto = models.ImageField(upload_to = url)
	Telefono = models.CharField(max_length = 15)
	Webpage = models.CharField(max_length = 20)
	Descripcion = models.TextField(max_length = 300)
	Direccion = models.CharField(max_length = 50)
	Nombre = models.CharField(max_length = 30)
	ApellidoP = models.CharField(max_length = 20)
	ApellidoM = models.CharField(max_length = 20)
	Estado = models.CharField(max_length = 30)
	Ciudad = models.CharField(max_length = 30)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def __unicode__(self):
	return self.user.username

#MODELO DE AUTOS
class Autos(models.Model):
	'''def url2(self, filename):
		ruta = "/images/anuncios/%s/"% (filename)
		return ruta'''

	Id_anuncio = models.AutoField(primary_key = True)
	Usuario = models.ForeignKey(User)
	Num_Serie = models.CharField(max_length = 20, unique = True) 
	Marca = models.CharField(max_length = 20, choices = (
		('Acura','Acura'),('Audi','Audi'),('BMW','BMW'),('Cadillac','Cadillac'),
		('Chevrolet','Chevrolet'),('Chrysler','Chrysler'),('Dodge','Dodge'),('Ford','Ford'),
		('GMC','GMC'),('Honda','Honda'),('Mazda','Mazda'),('Nissan','Nissan'),('Toyota','Toyota'),
		('Volkswagen','Volkswagen'),('Volvo','Volvo')
		))
	#--------------------------------------------------------------------
	Modelo = models.CharField(max_length = 20)
	Foto = models.ImageField(upload_to = 'images/anuncios/')
	Year = models.CharField(max_length = 4, choices=(
		('1990','1990'),('1991','1991'),('1992','1992'),('1993','1993'),('1994','1994'),
		('1995','1995'),('1996','1996'),('1997','1998'),('1999','1999'),('2000','2000'),
		('2001','2001'),('2002','2002'),('2003','2003'),('2004','2004'),('2005','2005'),
		('2006','2006'),('2007','2007'),('2008','2008'),('2009','2009'),('2009','2009'),
		('2010','2010'),('2011','2011'),('2012','2012'),('2013','2013'),('2014','2014')
		))
	#--------------------------------------------------------------------
	Transmision = models.CharField(max_length = 20,choices = (
		('Automatica', 'Automatica'),
		('Standard', 'Standard'),
		))
	#--------------------------------------------------------------------
	Cilindros = models.CharField(max_length = 20,choices = (
		('4', '4'),
		('6', '6'),
		('8', '8'),
		))
	#---------------------------------------------------------------------
	Combustible = models.CharField(max_length = 20,choices = (
		('Gasolina', 'Gasolina'),
		('Diesel', 'Diesel'),
		))
	#---------------------------------------------------------------------
	dos = '2'
	cuatro = '4'
	Puertas = models.CharField(max_length = 6,choices = (
		(dos,'2'),
		(cuatro,'4'),
		))
	Color = models.CharField(max_length = 20)
	Precio = models.DecimalField(max_digits = 20, decimal_places = 2)
	Ubicacion = models.CharField(max_length = 30)
	Comentarios = models.TextField(max_length = 300)
	Fecha = models.DateField(auto_now_add = True)
	Visitas = models.IntegerField(default = 0)
	NumReportes = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.Marca



#MODELO DE CLIENTES
class Calificacion(models.Model):
	UsuarioCalificador = models.ForeignKey(User, related_name = "UsuarioCalificador")
	UsuarioCalificado = models.ForeignKey(User, related_name = "UsuarioCalificado")
	Calificacion = models.IntegerField(choices = (
		(3,'Postiva'),(2,'Regular'),(1,'Negativa'),
		))
	Motivo = models.TextField()