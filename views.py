from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import Contact, BookingDetails
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        "variable": "this is all about me"
    }
   # return HttpResponse('this is home page')
    return render(request, 'index.html', context)


def add(request):
    return HttpResponse('suceesfully submited')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def signin(request):
    return render(request, 'signin.html')


def products(request):
    return render(request, 'products.html')


def cook(request):
    return render(request, 'cook.html')


def elderly(request):
    return render(request, 'elderly.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def ref2(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        location = request.POST.get('location')
        category = request.POST.get('category')
        work_hour = request.POST.get('work_hour')
        gender_preference = request.POST.get('gender_preference')
        total_people = request.POST.get('total_people')
        house_size = request.POST.get('house_size')
        budget = request.POST.get('budget')
        comment = request.POST.get('comment')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        booking = BookingDetails(email=email, mobile_no=mobile_no, location=location, category=category, work_hour=work_hour, gender_preference=gender_preference,
                                 total_people=total_people, house_size=house_size, budget=budget, comment=comment,
                                 f_name=f_name, l_name=l_name, address=address, zipcode=zipcode)
        booking.save()
        messages.success(request, 'Your Form Has Been Submitted.')
    return render(request, 'ref2.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Form Has Been Submitted.')

    return render(request, 'contact.html')
