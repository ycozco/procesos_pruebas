from django.db import models

class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField()
    correo_electronico = models.TextField(unique=True)
    password = models.TextField()
    tipo = models.TextField()
    status = models.TextField()

    class Meta:
        db_table = 'Usuarios'

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()

    class Meta:
        db_table = 'Categorias'  # Nombre de la tabla en la base de datos

class Leccion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    descripcion = models.TextField()
    contenido_texto = models.TextField()
    ruta_imagen = models.TextField()
    ruta_recurso = models.TextField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.TextField()

    class Meta:
        db_table = 'Lecciones'  # Nombre de la tabla en la base de datos

class Ejercicio(models.Model):
    id = models.AutoField(primary_key=True)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    enunciado = models.TextField()
    ruta_imagen = models.TextField()

    class Meta:
        db_table = 'Ejercicios'  # Nombre de la tabla en la base de datos

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    texto_respuesta = models.TextField()
    es_correcta = models.BooleanField()

    class Meta:
        db_table = 'Respuestas'  # Nombre de la tabla en la base de datos

# Resto de los modelos, sigue el mismo patrón para especificar los nombres de las tablas
class Evaluacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    calificacion = models.IntegerField()

    class Meta:
        db_table = 'Evaluaciones'  # Nombre de la tabla en la base de datos

class Resultado(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Resultados'

class Progreso(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    completada = models.BooleanField()

    class Meta:
        db_table = 'Progresos'

class Puntuacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()

    class Meta:
        db_table = 'Puntuaciones'
