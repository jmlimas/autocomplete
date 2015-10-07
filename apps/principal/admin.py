from django.contrib import admin
from .models import Alumno, Nota


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
	list_display = ( 'nombre','pais')
	search_fields = ('nombre',)



@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
	list_display = ( 'alumno','materia','calificacion')