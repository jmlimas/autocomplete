from django.views.generic import  CreateView,ListView
from .models import Alumno,Nota
from .forms  import AlumnoForm,NotaForm   
 
 
from django.http import HttpResponse
#from django.core import serializers 
import json
 
  

class AddAlumno(CreateView):
	model = Alumno
	form_class = AlumnoForm
	template_name = 'addAlumno.html'
	success_url = '/'


class AddNota2(CreateView):
	model = Nota 
	form_class = NotaForm
	template_name = 'addNotas2.html'
	success_url = '/list' 

	def post(self, request, *args, **kwargs):
		post = super(AddNota2, self).post(request, *args, **kwargs)
		alu = request.POST['q']
		mat = request.POST['materia']
		cali = request.POST['calificacion']
		Nota.objects.create(alumno=Alumno.objects.get(nombre=alu),materia=mat,calificacion=cali)
		return post


class AddNota1(CreateView):
	model = Nota
	form_class = NotaForm
	template_name = 'addNotas1.html'
	success_url = '/list'

class ListNotas(ListView):
	context_object_name = 'notas'
	template_name = 'listnotas.html'
	model = Nota

def ListaAlumnos_ajax(request):
	if request.is_ajax():
		palabra = request.GET.get('q','')
		alum = Alumno.objects.filter(nombre__icontains=palabra)
		results=[]
		for a in alum:
			alum_json={}
			alum_json['id'] = a.id
			alum_json['nombre'] = a.nombre
			results.append(alum_json)

		data_json = json.dumps(results)		 
	else:
		data_json='fail'
	mimetype="application/json"
	return HttpResponse(data_json,mimetype)
