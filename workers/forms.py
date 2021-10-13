from django import forms
from .models import Workers


class WorkersForm(forms.ModelForm):

    class Meta:
        model = Workers
        fields = '__all__'
        labels = {
            'fullname' : 'Nom et Prénoms',
            'work_code' : "Code de l'employé",
            'mobile' : 'Numéro de Téléphone',
            'position' : 'Position',
        },

    def __init__(self, *args, **kwargs):
        super(WorkersForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['fullname'].widget.attrs.update({'onkeyup': 'this.value = this.value.toUpperCase();'})
