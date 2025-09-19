from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from main.models import Trening
from .models import Registration,Registrationitem

@login_required
def add_to_registration(request,product_id):
    trening = get_object_or_404(Trening,id=product_id)
    registration,created=Registration.objects.get_or_create(user = request.user)
    registration_item,created = Registrationitem.objects.get_or_create(registration=registration,trening=trening)

    if not created:
        registration_item.quantity +=1
        registration_item.save()
    
    return redirect('registrastions_list')


@login_required
def registration_list(request):
    registration = Registration.objects.filter(user=request.user).first()
    registration_item = registration.items.all() if registration else[]
    total_price = sum(item.get_total_price() for item in registration_item)
    return render(request,'registration/registrations_list.html',{'registration_item':registration_item,'total_price':total_price})