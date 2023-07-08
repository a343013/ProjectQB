from django import forms
from .models import Agente, Inspector, Evaluacion

class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agente
        fields = ['nombre', 'equipo']

class InspectorForm(forms.ModelForm):
    class Meta:
        model = Inspector
        fields = ['nombre']

class EvaluacionForm(forms.ModelForm):
    # Opciones para los campos de pregunta
    OPCIONES_RESPUESTA = [
        ('si', 'Sí'),
        ('no', 'No'),
    ]

    # Definición de los campos del formulario
    pregunta1 = forms.ChoiceField(choices=OPCIONES_RESPUESTA, label='¿El agente se presentó de acuerdo al proceso?', widget=forms.Select(attrs={'class': 'form-control'}))
    pregunta2 = forms.ChoiceField(choices=OPCIONES_RESPUESTA, label='¿El agente identificó el problema raíz?', widget=forms.Select(attrs={'class': 'form-control'}))
    pregunta3 = forms.ChoiceField(choices=OPCIONES_RESPUESTA, label='¿El agente dio solución al problema del cliente?', widget=forms.Select(attrs={'class': 'form-control'}))
    pregunta4 = forms.ChoiceField(choices=OPCIONES_RESPUESTA, label='¿El agente registró toda la información necesaria sobre el caso?', widget=forms.Select(attrs={'class': 'form-control'}))
    pregunta5 = forms.ChoiceField(choices=OPCIONES_RESPUESTA, label='¿El agente se despidió conforme al proceso?', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Evaluacion
        fields = ['agente', 'inspector', 'fecha', 'interaccion', 'pregunta1', 'pregunta2', 'pregunta3', 'pregunta4', 'pregunta5']
