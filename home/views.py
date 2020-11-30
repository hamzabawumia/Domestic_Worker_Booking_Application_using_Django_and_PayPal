from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.contrib import messages
from .models import *
import json
from django.http import JsonResponse
from .utils import cookieCart, cartData, guestOrder
from home.models import BookingDetails
from django.contrib.auth import authenticate, login
from django.forms import inlineformset_factory
import requests

import random

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        number = request.POST.get('number')
        marital_status = request.POST.get('marital_status')
        language = request.POST.get('language')
        job = request.POST.get('job')
        religion = request.POST.get('religion')
        pan_card = request.POST.get('pan_card')
        aadhar_card = request.POST.get('aadhar_card')
        photo = request.POST.get('photo')

        sitter = Sitter(fname=fname, lname=lname, email=email, password=password, address=address, city=city, state=state, zipcode=zipcode, age=age, gender=gender,
                        number=number, marital_status=marital_status, language=language, job=job, religion=religion, pan_card=pan_card, aadhar_card=aadhar_card, photo=photo)

        sitter.save()
    return render(request, 'register.html')


def loginpage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(
                    request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully logged in')
                    return redirect('/')
                else:
                    messages.info(request, 'Username Or password is incorrect')
            context = {}
            return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.warning(request, "Account successfully logout")
    return redirect('login')


def signup(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'signup.html', context)


def Baby(request):
    allsitter = Sitter.objects.all()
    context={'allsitter':allsitter}  
    return render(request, 'Baby.html',context)


def cook(request):
    return render(request, 'cook.html')


def elderly(request):
    return render(request, 'elderly.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        mobile_no = request.POST.get('mobile_no')      
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, mobile_no=mobile_no, service=service,
                        message=message, date=datetime.date.today())
        contact.save()
        messages.success(request, 'Your Form Has Been Submitted.')


    return render(request, 'contact.html')


def ref(request):
    
    return render(request, 'ref.html')




def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    if request.method == 'POST':
        otp = request.POST.get('text')
        if int(otp) == key:
            messages.success(request, 'Your Form Has Been Submitted.')
            return render(request, 'store.html', context)
        else:
            messages.success(request, 'Wrong OTP!!!Try Again')
            return render(request, 'OTP.html')
    
    


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)


def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity(orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity(orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],

        )

    return JsonResponse('Payment completed', safe=False)


def otp_verify(request):
    global key
    # phone_number = request.data.get('mobile_no')
    if request.method == 'POST':
        email = request.POST.get('email')
        phone_number = request.POST.get('mobile_no')
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
        booking = BookingDetails(email=email, mobile_no=phone_number, location=location, category=category, work_hour=work_hour, gender_preference=gender_preference,
                                total_people=total_people, house_size=house_size, budget=budget, comment=comment,
                                f_name=f_name, l_name=l_name, address=address, zipcode=zipcode)
        #phone_number = request.POST.get('mobile_no')
        booking.save()
        phone = str(phone_number)
        key = send_otp(phone)
        return render(request, 'OTP.html')


global key


def send_otp(phone):
    """
    This is an helper function to send otp to session stored phones or
    passed phone number as argument.
    """

    if phone:

        # key = otp_generator()
        key = random.randint(999, 9999)
        phone = str(phone)
        otp_key = str(key)

        link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=563027b1-291e-11eb-83d4-0200cd936042&to={phone}&from=ABCDEZ&templatename=Harsh&var1={phone}&var2={otp_key}'

        result = requests.get(link, verify=False)
        print("***********")
        print(result)
        print("***********")
        return key
    else:
        return False
