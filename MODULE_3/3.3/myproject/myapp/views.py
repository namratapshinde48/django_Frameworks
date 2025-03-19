from django.shortcuts import render
from .forms import BookingForm

def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()

    return render(request, "booking.html", {"form": form})
