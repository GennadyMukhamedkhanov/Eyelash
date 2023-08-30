from django import forms
from my_site.models import Service

class HomeForm(forms.Form):
    data = Service.objects.all()
    tp = ((v.id, v.name) for v in data)
    name_pr = forms.ChoiceField(label='Название процедуры', choices=tp)








#207