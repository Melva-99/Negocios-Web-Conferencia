from django.db import models


'''
    Tipos de datos para los campos de los modelos:
    -Todos los campos se obtienen de models
    -Tipo CharField(max_lenght=25, default='Jack', null=true,blank=true)
    -> TextField()
    -> IntegerField()
    ->DecimalField(max_digits=5, decimal_places=2)
    -> PositiveIntegerField()
    -> SamllIntegerField()
    -> BooleanField(default=true)
    -> EmailField()
    -> ImageField(upload_to='fotos')
    -> FileField(upload_to='archivos')
    -> SlugField() : tesla ha afectado el precio del bitcoin tesla-ha-afectado-

    Campos para establecer relaciones entre modelos:
    >ForeignKey(Categoria,on_delete='models.CASCADE') 'models.SET_NULL'=valor huerfano on_delete=dependiendo de lo que pasa va ocurrir en el secundario
    ->OneToOneField()
    ->ManyToManyField()

'''

class Conferencista(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    experiencia = models.TextField()

    def __str__(self):
        return self.nombre

#guardar participantes en la base de datos
class Conferencia(models.Model):
    nombre = models.CharField(max_length=35)
    fecha_registro = models.DateTimeField(auto_now_add=True) #se agrega la fecha del sistema
    fecha = models.DateField()
    hora = models.TimeField()
    conferencista = models.ForeignKey(Conferencista, on_delete=models.CASCADE, null=true)

    def __str__(self):
        return self.nombre
