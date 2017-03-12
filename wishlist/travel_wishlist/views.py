from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Place
from .forms import NewPlaceForm, NewInformationForm


def place_list(request):

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')
    places = Place.objects.all()
    form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'form' : form})


def places_visited(request, pk):
    visited = get_object_or_404(Place, pk=pk)
    return render(request, 'travel_wishlist/visited.html', {'visited' :visited})


def place_is_visited(request):
    pk = request.POST.get('pk')
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = NewInformationForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.visited = True
            place.save()

    return redirect('place_list')

def place_list_information(request, pk):
    info = get_object_or_404(Place, pk=pk)
    form = NewInformationForm()
    return render(request, 'travel_wishlist/information.html', {'info' :info, 'form' : form})
