from django.db.models import Sum, F, Case, When
from django.shortcuts import render

from .forms import TruckForm
from .models import Truck


def index(request):
    truck_model_selection = request.POST.get('select', '')

    if truck_model_selection == 'Все':
        trucks_list = Truck.objects.all()
    else:
        trucks_list = Truck.objects.filter(truck_model__name=truck_model_selection)

    trucks_list = trucks_list.annotate(weight_count=Sum('cargo__weight'))

    # Подсчет перегруза в %
    trucks_list = trucks_list.annotate(
        overload_count_per=Case(When(
            truck_model__max_load_capacity__lt=F('weight_count'),
            then=Sum('cargo__weight') * 100 / F('truck_model__max_load_capacity') - 100),
            default=0)
    )

    form = TruckForm(request.POST)

    context = {"trucks_list": trucks_list, 'form': form, 'truck_model_selection': truck_model_selection}

    return render(request, "trucks/index.html", context)
