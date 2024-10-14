from django import forms

from aplication.core.models import Doctor, Medications

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        #        inputtext               select
        fields=['first_name','last_name','profession','clinic','sex','birth_date','address','is_active']
        
class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medications
        # Campos del formulario para el modelo de medicamentos
        fields = ['description', 'price', 'stock', 'is_active']  # Reemplazando campos del doctor por los del medicamento
             