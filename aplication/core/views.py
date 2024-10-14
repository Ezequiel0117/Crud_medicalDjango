from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from aplication.core.forms import DoctorForm, MedicationForm
from aplication.core.models import Doctor, Medications
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

         
def home(request):
   data={"title":"Medical","title1":"Sistema Medico Online"}
   #return HttpResponse("<h1>Pantalla de Inicio</h1>")
   #return JsonResponse(data)
   return render(request,'core/home.html',data)

# def doctor_List(request):
#     data={"title":"Medical","title1":"Consulta de Doctores"}
#     doctores = Doctor.objects.all() # queryset[d1,d2,d3]
#     for doctor in doctores:
#        print(doctor.first_name," ",doctor.clinic.name)
#     data["doctores"]=doctores
#     print(data)
#     return render(request,"core/doctor/list.html",data)

class Doctor_ListView(ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    context_object_name = 'doctor_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Sistema Medico Online'
        return context


class MedicamentListView(LoginRequiredMixin,ListView):
    model = Medications
    template_name = 'core/doctor/list_medicament.html'
    context_object_name = 'medicament_list'
    login_url = '/signin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Sistema Medico Online'
        return context

    
# def doctor_create(request):
#    data = {"title": "Doctores","title1": "Añadir Doctores"}
#    if request.method == "POST":
#       print(request.POST)
#       form = DoctorForm(request.POST)
#       if form.is_valid():
#          form.save()
#          return redirect("core:doctor_list")
#       else:
#          data["form"] = form
#          data["error"] = "Error al crear el Doctor."
#          return render(request, "core/doctor/form.html", data)
#    else:
#       form = DoctorForm()
#       # <tr>inputtext,select <\>
#       data["form"] = form
#    print(form)
#    return render(request, "core/doctor/form.html", data)

class Doctor_CreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list') #Redireccion a la lista de doctores
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Crear un nuevo doctor'
        return context
    
    
class Medicament_CreateView(CreateView):
    model = Medications
    form_class = MedicationForm
    template_name = 'core/doctor/form_medicament.html'
    success_url = reverse_lazy('core:medicament_list')  # Redirecciona a la lista de medicamentos
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Crear nuevo medicamento'
        context['title3'] = 'Grabar medicamento'
        return context
    
    def form_valid(self, form): 
        # Asigna el usuario autenticado al campo 'user' del modelo Medications
        form.instance.user = self.request.user
        return super().form_valid(form)

 
# def doctor_update(request,id):
#    data = {"title": "Doctores","title1": "Editar Doctor"}
#    doctor = Doctor.objects.get(pk=id)# doctor1
#    if request.method == "POST":
#       form = DoctorForm(request.POST,instance=doctor)
#       if form.is_valid():
#          form.save()
#          return redirect("core:doctor_list")
#       else:
#          data["form"] = form
#          data["error"] = "Error al editar el Doctor."
#          return render(request, "core/doctor/form.html", data)
#    else:
#       form = DoctorForm(instance=doctor)
#       data["form"] = form
#    print(form)
#    return render(request, "core/doctor/form.html", data)

class Doctor_UpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list') #Redireccion a la lista de doctores
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Editar doctor'
        return context
    
    

class Medicament_UpdateView(UpdateView):
    model = Medications
    form_class = MedicationForm
    template_name = 'core/doctor/form_medicament.html'
    success_url = reverse_lazy('core:medicament_list') #Redireccion a la lista de doctores
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Editar medicamento'
        return context
    
    def form_valid(self, form): 
        # Asigna el usuario autenticado al campo 'user' del modelo Medications
        form.instance.user = self.request.user
        return super().form_valid(form)

# def doctor_delete(request,id):
#    doctor = Doctor.objects.get(id=id)
#    data = {"title":"Eliminar","title1":"Eliminar Doctor","doctor":doctor}
#    if request.method == "POST":
#       doctor.delete()
#       return redirect("core:doctor_list")
#    return render(request, "core/doctor/delete.html", data)

class doctor_DeleteView(DeleteView):
    model = Doctor
    template_name = 'core/doctor/delete.html'
    success_url = reverse_lazy('core:doctor_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'
        context['title1'] = 'Eliminar doctor'
        return context
    
class Medicament_DeleteView(DeleteView):
    model = Medications
    template_name = 'core/doctor/delete_medicament.html'
    success_url = reverse_lazy('core:medicament_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'
        context['title1'] = 'Eliminar Medicamento'
        context['medication'] = self.object  # Renombrar el objeto a 'medication'
        return context  # Corrección aquí, retornas solo 'context'
    
    

def signup(request):
    if request.method == "GET":
        return render(request, "core/signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password1'])
                user.save()
                login(request, user)  # Crear cookie y redireccionarlo
                # Return para una vez que termine ahi una vez que se guarde el usuario
                return redirect('core:home')
            except IntegrityError:
                return render(request, "core/signup.html", {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        return render(request, "core/signup.html", {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })
        
def signout(request):
    logout(request)
    # Return para redireccionar al home después de cerrar sesión
    return redirect('core:home')


def siging(request):
    if request.method == 'GET':
        return render(request, "core/signin.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],password=request.POST
            ['password'])
        if user is None:
            return render(request, 'core/signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('core:home')

