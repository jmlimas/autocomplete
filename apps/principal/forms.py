from django import forms
from models import Alumno,Nota  
 
 
class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = '__all__'


class NotaForm(forms.ModelForm):
	class Meta:
		model = Nota
		fields = '__all__'