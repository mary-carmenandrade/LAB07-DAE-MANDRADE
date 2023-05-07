from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('eliminar_alumno/<int:alumno_id>', views.EliminarAlumnoView.as_view(), name='eliminar_alumno'),
    path('profesor/', views.ProfesorView.as_view(),name='profesor'),
    path('eliminar_profesor/<int:profesor_id>', views.EliminarProfesorView.as_view(), name='eliminar_profesor'),
]