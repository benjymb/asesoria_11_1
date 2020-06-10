# Pasos para crear un nuevo proyecto en Django
1. Ejecutar `django-admin startproject <nombre_del_proyecto>` (Reemplazar <nombre_del_proyecto>)
2. Ingresar a la carpeta que se creo y tiene el nombre del proyecto.
3. Ejecutar `django-admin startapp <nombre_de_la_aplicacion>` (Reemplazar <nombre de la aplicacion>)
4. Aniadir en el archivo <nombre_del_proyecto>/<nombre_del_proyecto>/settings.py, debajo de INSTALLED_APPS, el nombre de la aplicacion creada.
5. Crear una nueva vista (tomar como ejemplo la clase IndexView de main/views.py )
6. Aniadir una nueva ruta en <nombre_del_proyecto>/<nombre_del_proyecto>.urls.py
7. Ejecutar python manage.py runserver