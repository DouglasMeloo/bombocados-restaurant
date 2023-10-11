from django.shortcuts import render, redirect
from .models import Reservation, MenuItem
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Table reserved successfully!')
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'bookings/reserve.html', {'form': form})


def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'bookings/menu.html', {'menu_items': menu_items})
