from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm
#create your views here

def home(request):
    return render(request,"nezx/signin.html") 


def signup(request):

   if request.method == 'POST':
       username = request.POST['username']
       fname = request.POST['fname']
       lname = request.POST['lname']    
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']

       myuser = User.objects.create_user(username, email, pass1)
       myuser.first_name = fname
       myuser.last_name= lname
       
       myuser.save()

       messages.success(request, "Your account has been successfully created")

       return redirect('signin')

   return render(request,"nezx/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name 
            return render(request, "nezx/index.html",{"fname":fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
   
    return render(request,"nezx/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("signin")

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For example, save the customer to the database
            return redirect('success_page')  # Redirect to a success page
    else:
        form = CustomerForm()
    return render(request, 'nezx/customer_form.html', {'form': form})

