from django.db import models
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
#inherit from models.Model

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Sitter(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    rate = models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    desc = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    address = models.TextField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    marital_status = models.CharField(max_length=150)
    language = models.CharField(max_length=150)
    job = models.CharField(max_length=150)
    religion = models.CharField(max_length=150)

    pan_card = models.ImageField(
        null=True, blank=True)
    aadhar_card = models.ImageField(
        null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.fname+self.lname


    @property
    def photoURL(self):
        try:
            url = self.photo.url
        except:
            url = ' '
        return url



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ' '
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total  

    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping= True
        return shipping                     



class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=(self.product.price * self.quantity)
        return total


class OrderSitter(models.Model):
    sitter = models.ForeignKey(
        Sitter, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_sum(self):
        sum = (self.sitter.rate * self.quantity)
        return sum




class ShippingAddress(models.Model):
    cutomer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



class BookingDetails(models.Model):
    email = models.EmailField(max_length=255)
    mobile_no = models.IntegerField()
    location = models.TextField()
    category = models.TextField()
    work_hour = models.IntegerField()
    gender_preference = models.TextField(default="none")
    total_people = models.IntegerField()
    house_size = models.CharField(max_length=255, default="no comment")
    budget = models.CharField(max_length=255)
    comment = models.TextField()
    f_name = models.TextField()
    l_name = models.TextField()
    address = models.CharField(max_length=500)
    zipcode = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile_no = models.CharField(max_length=12)
    service = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()
