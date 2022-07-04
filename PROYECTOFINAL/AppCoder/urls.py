from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('sedes', views.sedes, name="Sedes"),
    path('profesores', views.profesores, name="Profesores"),
    path('clases', views.clases, name="Clases"),
    path('socios', views.socios, name="Socios"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),


    path('sede/list', views.SedeList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.SedeDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.SedeCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.SedeUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.SedeDelete.as_view(), name='Delete'),


    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),


    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),


    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),