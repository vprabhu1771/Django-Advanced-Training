from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, State, City


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'backend/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'backend/home.html', {'form': form})


# AJAX
def load_states(request):
    country_id = request.GET.get('country_id')

    context = {
        "states": State.objects.filter(country_id=country_id).all()
    }

    # http://127.0.0.1:8000/ajax/load-states/?country_id=2
    # return JsonResponse(list(states.values('id', 'name')), safe=False)
    return render(request, 'backend/state_dropdown_list_options.html', context)

# AJAX
def load_cities(request):
    state_id = request.GET.get('state_id')

    context = {
        "cities": City.objects.filter(state_id=state_id).all()
    }

    # http://127.0.0.1:8000/ajax/load-cities/?state_id=2
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    return render(request, 'backend/city_dropdown_list_options.html', context)

