from django.shortcuts import render,HttpResponse
import datetime
from django.contrib import messages
from .models import *
import json
from django.http import JsonResponse
from .utils import cookieCart,cartData,guestOrder

# Create your views here.

def index(request):
    return render(request,'index.html')

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

        sitter = Sitter(fname=fname, lname=lname, email=email, password=password, address=address, city=city, state=state, zipcode=zipcode, age=age, gender=gender, number=number, marital_status=marital_status, language=language, job=job, religion=religion, pan_card=pan_card, aadhar_card=aadhar_card, photo=photo)

        sitter.save()
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def signin(request):
    return render(request,'signin.html')

def baby(request):
    return render(request,'baby.html')

def cook(request):
    return render(request,'cook.html')

def elderly(request):
    return render(request,'elderly.html')

def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')



def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store.html',context)



def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context={'items':items,'order':order,'cartItems':cartItems}    
    return render(request,'cart.html',context)    



def checkout(request):  

    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']

    context={'items':items,'order':order,'cartItems':cartItems}     
    return render(request,'checkout.html',context)    



def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print('Action:',action)
    print('productId:',productId)

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created=OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity(orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity(orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()        

    return JsonResponse('Item was added',safe=False)


def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        

        

    else:
        customer,order=guestOrder(request,data)
        

    total=float(data['form']['total'])
    order.transaction_id=transaction_id

    if total == order.get_cart_total:
        order.complete=True
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

    return JsonResponse('Payment completed',safe=False)
