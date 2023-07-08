from django.db import models


# Create your models here.
class Agente(models.Model):
    nombre = models.CharField(max_length=255)
    equipo = models.CharField(max_length=255)

    def __str__(self):
        txt = "Agente: {0}"
        return txt.format(self.nombre)

class Inspector(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        txt = "Inspector: {0}"
        return txt.format(self.nombre)

class Evaluacion(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.SET_NULL, null=True, related_name='evaluaciones')
    inspector = models.ForeignKey(Inspector, on_delete=models.SET_NULL, null=True, related_name='evaluaciones')
    fecha = models.DateField()
    interaccion = models.TextField()
    pregunta1 = models.CharField(max_length=2, default='no', verbose_name='¿El agente se presentó de acuerdo al proceso?')  # Agrega el parámetro default con el valor predeterminado
    pregunta2 = models.CharField(max_length=2, default='no', verbose_name='¿El agente identificó el problema raíz?')
    pregunta3 = models.CharField(max_length=2, default='no', verbose_name='¿El agente dio solución al problema del cliente?')
    pregunta4 = models.CharField(max_length=2, default='no', verbose_name='¿El agente registró toda la información necesaria sobre el caso?')
    pregunta5 = models.CharField(max_length=2, default='no', verbose_name='¿El agente se despidió conforme al proceso?')
    puntaje = models.IntegerField()

    def calcular_puntaje(self):
        puntaje = 0
        if self.pregunta1 == 'si':
            puntaje += 20
        if self.pregunta2 == 'si':
            puntaje += 20
        if self.pregunta3 == 'si':
            puntaje += 20
        if self.pregunta4 == 'si':
            puntaje += 20
        if self.pregunta5 == 'si':
            puntaje += 20
        return puntaje

    def __str__(self):
        txt = "Interaccion: {0}. Puntaje: {1}"
        return txt.format(self.interaccion, self.puntaje)