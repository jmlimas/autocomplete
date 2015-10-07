from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^addAlumno/$',views.AddAlumno.as_view(),name='add_alumno'),  
	url(r'^addnota1/$',views.AddNota1.as_view(),name='add_nota1'),
	url(r'^addnota2/$',views.AddNota2.as_view(),name='add_nota2'),
	url(r'^list/$',views.ListNotas.as_view(),name='list_nota'),	
	url(r'^buscanombre_url/$','apps.principal.views.ListaAlumnos_ajax',name='aj_busanombre'),
   
]