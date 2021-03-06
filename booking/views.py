from itertools import groupby

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.db import transaction

from django.db.models import Min, Max, Count, Sum, Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import BookRoom, BookCar, BookBike, BookingItem, BookingContact, Booking

from hotels.models import Hotel
from hotels.forms import HotelFilterForm

from .forms import CarFilterForm, BikeFilterForm, BookForm

# Create your views here.
def search_hotel(request):
    params = request.GET

    # BUILDING QUERIES
    q = Hotel.objects
    prices = q.aggregate(max=Max('room__price'),min=Min('room__price'))

    if params.get('c'):
        q = q.filter(category__in=params.getlist('c'))

    if params.get('rt'):
        q = q.filter(room__roomtype__roomtype__in=params.getlist('rt'))

    if params.get('price'):
        q = q.filter(room__price__lte=params.get('price'))

    hotels = q.annotate(min_price=Min('room__price'))

    form = HotelFilterForm(params)

    data = {
        'hotels': hotels,
        'form' : form,
        'active_tab': 'hotels',
        'meta': {
            'prices': prices
        }
    }

    return render(request, 'booking/hotels/results.html', data)


def search_hotel_detail(request, slug):

    hotel = Hotel.objects.get(slug=slug)

    q = BookRoom.objects.filter(hotel=hotel).order_by('price')

    if request.GET.get('rt'):
        q = q.filter(roomtype__roomtype__in=request.GET.getlist('rt'))

    rooms = q.order_by('category').all()

    min_price = q.aggregate(min=Min('price'))

    categories = dict((k, list(g)) for k, g in groupby(rooms, key=lambda x: x.category))

    # bring all images of hotel
    image_list = hotel.images.all()

    data = {
        'hotel': hotel,
        'image_list': image_list,
        'categories': categories,
        'meta' : {
            'prices': min_price
        }
    }

    return render(request, 'booking/hotels/detail.html', data)

def search_car(request):
    params = request.GET
    form = CarFilterForm(params)

    # get dates from url
    checkin = params.get('checkin')
    checkout = params.get('checkout')

    booked_ids = _get_booked_ids(BookCar, checkin, checkout)

    # BUILDING QUERIES
    q = BookCar.objects.exclude(id__in=booked_ids)

    prices = q.aggregate(max=Max('price'),min=Min('price'))

    if params.get('t'):
        q = q.filter(category__in=params.getlist('t'))
    if params.get('cc'):
        cc  = [int(x) for x in params.get('cc').split('-')]
        if len(cc) == 2:
            q = q.filter(cc__gte=cc[0]).filter(cc__lte=cc[1])
        else:
            q = q.filter(cc__gte=cc[0])
    if params.get('price'):
        q = q.filter(price__lte=params.get('price'))


    cars = q.order_by('model').all()

    data = {
        'cars' : cars,
        'form' : form,
        'active_tab': 'cars',
        'meta' : {
            'prices': prices
        }
    }

    return render(request, 'booking/cars/results.html', data)

def search_car_detail(request, slug):

    q = BookCar.objects.order_by('price')

    car = q.get(slug=slug)

    # bring all images of cars
    image_list = car.images.all()

    data = {
        'car': car,
        'image_list': image_list,
    }

    return render(request, 'booking/cars/detail.html', data)

def search_bike(request):
    params = request.GET
    form = BikeFilterForm(params)

    # get dates from url
    checkin = params.get('checkin')
    checkout = params.get('checkout')

    booked_ids = _get_booked_ids(BookBike, checkin, checkout)
    # BUILDING QUERIES
    q = BookBike.objects.exclude(id__in=booked_ids)


    prices = q.aggregate(max=Max('price'),min=Min('price'))

    if params.get('c'):
        q = q.filter(category__in=params.getlist('c'))
    if params.get('cc'):
        bcc  = [int(x) for x in params.get('cc').split('-')]
        if len(bcc) == 2:
            q = q.filter(cc__gte=bcc[0]).filter(cc__lte=bcc[1])
        else:
            q = q.filter(cc__gte=bcc[0])
    if params.get('price'):
        q = q.filter(price__lte=params.get('price'))


    bikes = q.order_by('model').all()

    data = {
        'bikes' : bikes,
        'form' : form,
        'active_tab': 'bikes',
        'meta' : {
            'prices': prices
        }
    }

    return render(request, 'booking/bikes/results.html', data)


def search_bike_detail(request, slug):
    q = BookBike.objects.order_by('price')

    bike = q.get(slug=slug)

    image_list = bike.images.all()

    data = {
        'bike': bike,
        'image_list': image_list,
    }

    return render(request, 'booking/bikes/detail.html', data)


def search_package(request):
    pass

def book(request, what):

    dates = {
        "checkin": request.session.get('checkin'),
        "checkout": request.session.get('checkout')
    }

    if not dates["checkin"]:
        return HttpResponseBadRequest()

    bike = None
    car = None
    rooms = None

    roomids = request.session.get('rooms')
    rental = request.session.get('rental')

    if what == 'hotel' or request.GET.get('from') == 'hotel':
        rooms = BookRoom.objects.filter(id__in=roomids).all()

    if what == 'car' and rental["type"] == 'car':
        car = BookCar.objects.get(pk=rental["id"])
    elif what == 'bike' and rental["type"] == 'bike':
        bike = BookBike.objects.get(pk=rental["id"])

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                with transaction.atomic():
                    # make the booking
                    booking = _process_data(request, form)
                    # add boooking items
                    if car:
                        car.add_item(booking, dates)
                    if bike:
                        bike.add_item(booking, dates)
                    if rooms:
                        for room in rooms:
                            room.add_item(booking, dates)

                    # redirect to a new URL:

                    return render(request, 'booking/book/thanks.html')
            except Exception as e:
                print (str(e))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    data = {
        'form': form,
        'dates': dates,
        'rooms': rooms,
        'bike': bike,
        'car': car
    }

    return render(request, 'booking/book/index.html', data)

@require_POST
def add_rental(request):
    params = request.POST

    checkin = params.get('checkin')
    checkout = params.get('checkout')
    rentalid = params.get('rental')
    rentaltype = params.get('type')

    request.session["rental"] = {
        "type": rentaltype,
        "id": rentalid
    }

    request.session['checkin'] = checkin
    request.session['checkout'] = checkout
    # if we came from hotel pass the param
    if params.get('from'):
        url = "%s?from=%s" % (reverse('booking:book', kwargs={'what': rentaltype}), params.get('from') )
    else:
        url = reverse('booking:book', kwargs={'what': rentaltype})

    return HttpResponseRedirect(url)

@require_POST
def add_room(request):
    params = request.POST

    checkin = params.get('checkin')
    checkout = params.get('checkout')

    request.session['rooms'] = params.getlist('room')
    request.session['checkin'] = checkin
    request.session['checkout'] = checkout

    if params.get('from'):
        url = "%s?checkin=%s&checkout=%s&from=%s" % (reverse('booking:search_car'),
                checkin, checkout, params.get('from'))
    else:
        url = reverse('booking:book', kwargs={ 'what': 'hotel'})

    return HttpResponseRedirect(url)

def _get_booked_ids(model, checkin, checkout):
    # (polymorphism) getting car type from the relation(inside has car/bike/rooms)
    bike_content_type = ContentType.objects.get_for_model(model)

    return BookingItem.objects.filter(
        (Q(check_in__gte=checkin) & Q(check_in__lte=checkout)) |
        (Q(check_out__gte=checkin) & Q(check_out__lte=checkout)) |
        (Q(check_in__lte=checkin) & Q(check_out__gte=checkout)),
        Q(content_type__pk=bike_content_type.id)
        ).values_list('object_id', flat=True)

def _get_user(r, email):
    user = None
    if r.user.is_authenticated:
        user =  r.user
    else:
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            print (str(e))

    return user


def _process_data(request, form):
    f = form.cleaned_data
    user = _get_user(request, f["email"])
    print(user)

    client = BookingContact(email=f["email"],
            first_name=f["fname"],
            last_name=f["lname"],
            phone=f["phone"])

    print(client)
    if user:
        client.user = user

    client.save()

    booking = Booking(user=client)
    booking.save()

    return booking


def thanku(request):
    return  render(request, 'booking/book/thanks.html')

