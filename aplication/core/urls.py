from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from aplication.core import views
 
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # ruta principal
  path('', views.home,name='home'),
  # rutas de doctores
  path('doctor_list/', views.doctor_ListView.as_view(),name="doctor_list"),
  path('doctor_create/', views.Doctor_CreateView.as_view(),name="doctor_create"),
  path('doctor_update/<int:pk>/', views.Doctor_UpdateView.as_view(),name='doctor_update'),
  path('doctor_delete/<int:pk>/', views.doctor_DeleteView.as_view(),name='doctor_delete'),
  path('medicament_list/', views.medicament_ListView.as_view(),name="medicament_list"),
  path('medicament_create/', views.Medicament_CreateView.as_view(),name="medicament_create"),
  path('medicament_update/<int:pk>/', views.Medicament_UpdateView.as_view(),name='medicament_update'),
  path('medicament_delete/<int:pk>/', views.medicament_DeleteView.as_view(),name='medicament_delete'),
  path('signup/', views.signup, name='signup'),
  path('logout/', views.signout, name='logout'),
  path('signin/', views.siging, name='signin'),
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


