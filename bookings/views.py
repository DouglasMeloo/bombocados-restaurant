from django.shortcuts import render, redirect
from .models import Reservation, MenuItem
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# @login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Table reserved successfully!')
            return redirect('home')
        return render(request, 'reserve.html')

    print("here")
    return render(request, 'reserve.html')


def menu_view(request):
    # menu_items = MenuItem.objects.all()
    # all()  # BO de SQL
    return render(request, 'menu.html')

def register_view(request):
    return render(request, 'register.html')