from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from aplication.core import views
 
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # ruta principal
  path('', views.home,name='home'),
  # rutas de doctores
  path('doctor_list/', views.Doctor_ListView.as_view(),name="doctor_list"),
  path('doctor_create/', views.Doctor_CreateView.as_view(),name="doctor_create"),
  path('doctor_update/<int:pk>/', views.Doctor_UpdateView.as_view(),name='doctor_update'),
  path('doctor_delete/<int:pk>/', views.doctor_DeleteView.as_view(),name='doctor_delete'),
  path('medicament_list/', views.MedicamentListView.as_view(), name="medicament_list"),
  path('medicament_create/', views.Medicament_CreateView.as_view(),name="medicament_create"),
  path('medicament_update/<int:pk>/', views.Medicament_UpdateView.as_view(),name='medicament_update'),
  path('medicament_delete/<int:pk>/', views.Medicament_DeleteView.as_view(),name='medicament_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


