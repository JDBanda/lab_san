from django.forms import ModelForm
from .models import Paciente, renglonServicio, Medico


class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
        fields = ("__all__")


class renglonServicioForm(ModelForm):

    class Meta:
        model = renglonServicio
        fields = ("__all__")


class MedicoForm(ModelForm):

    class Meta:
        model = Medico
        fields = ("__all__")
