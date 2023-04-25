from django import forms

from trucks.models import TruckModel


class TruckForm(forms.Form):
    CHOICES = [
        ("Все", "Все"),

    ]

    CHOICES += [(truck.name, truck.name) for truck in TruckModel.objects.all()]

    select = forms.CharField(widget=forms.Select(choices=CHOICES), label="Модель", required=False)
