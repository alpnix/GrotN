from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from authentication.models import Landlord
from .models import House 

# Create your views here.

def profile(request):
    return render(request, 'landlord/profile.html')

def houses(request):
    landlord = Landlord.objects.filter(user=request.user).first()
    houses = House.objects.filter(landlord=landlord)

    return render(request, 'landlord/houses.html', {'houses': houses})  

def matches(request):
    return render(request, 'landlord/matches.html')

def edit_house(request, house_id):
    house = House.objects.filter(house_id=house_id).first()

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        square_meters = request.POST.get('size')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        city = request.POST.get('city')
        district = request.POST.get('district')
        address = request.POST.get('address')
        hosting_roommates = False if request.POST.get('roommate')=="no" else True
        additional_info = request.POST.get('info')
        available = True
        landlord = Landlord.objects.filter(user=request.user).first()

        values = {
            'title': title,
            'price': price,
            'square_meters': square_meters,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'city': city,
            'district': district,
            'address': address,
            'hosting_roommates': hosting_roommates,
            'additional_info': additional_info,
            'available': available,
            'landlord': landlord
        }

        try: 
            House(**values).full_clean()
        except ValidationError as e: 
            print(e.message_dict)
            return render(request, 'landlord/edit_house.html', {'house': vars(house), 'error': e.message_dict})
        else: 
            House.objects.filter(house_id=house_id).update(**values)

        return redirect('landlord:houses')
    

    return render(request, 'landlord/edit_house.html', {'house': vars(house)})

def new_house(request): 
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        square_meters = request.POST.get('size')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        city = request.POST.get('city')
        district = request.POST.get('district')
        address = request.POST.get('address')
        hosting_roommates = False if request.POST.get('roommate')=="no" else True
        additional_info = request.POST.get('info')
        available = True
        landlord = Landlord.objects.filter(user=request.user).first()
        house = House(title=title, price=price, square_meters=square_meters, bedrooms=bedrooms, bathrooms=bathrooms, city=city, district=district, address=address, hosting_roommates=hosting_roommates, additional_info=additional_info, available=available, landlord=landlord)

        try: 
            house.full_clean()
        except ValidationError as e: 
            print(e.message_dict)
            return render(request, 'landlord/new_house.html', {'house': vars(house), 'error': e.message_dict})
        else: 
            house.save()

        return redirect('landlord:houses')
    
    return render(request, 'landlord/new_house.html')