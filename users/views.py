from django.shortcuts import render, redirect
from django.db.models import F
from .models import client
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.messages import get_messages
import datetime
from django.db import IntegrityError
from django.http import HttpResponse

# Create your views here.
def home(request):
    user_email = request.session.get('user_email')

    if user_email:
        return render(request, 'user/home.html', {'email': user_email})
    else:
        messages.error(request, 'Authentication Failed! Login to proceed')
        return redirect('login')

def login(request):
    storage = get_messages(request)
    storage.used = True  

    if request.method == "POST":
        client_email = request.POST.get('email')
        client_password = request.POST.get('password')

        # Check if the email exists
        if client.objects.filter(Email=client_email).exists():

            row = client.objects.get(Email=client_email)

            if check_password(client_password, row.password):
                request.session['user_email'] = client_email
                messages.success(request, 'Welcome! You have been logged in successfully')
                return redirect('profile')
            else:
                messages.error(request, 'Incorrect password. Please try again.')
                return redirect('login')
        else:
            messages.error(request, 'Email does not exist in our records!')
            return redirect('login')

    return render(request, 'user/login.html')

def register(request):
    storage = get_messages(request)
    storage.used = True
    
    if request.method == "POST":
        client_fname = request.POST.get('first_name')
        client_sname = request.POST.get('second_name')
        client_email = request.POST.get('email')
        client_phone = request.POST.get('phone')
        client_password = request.POST.get('password')

        if not all([client_fname, client_sname, client_email, client_phone, client_password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'user/register.html')
        
        if client.objects.filter(Email=client_email).exists():
            messages.error(request, 'Email already exists. Use a different one')
            return render(request, 'user/register.html')
        
        if client.objects.filter(phone=client_phone).exists():
            messages.error(request, 'Phone number already exists')
            return render(request, 'user/register.html')

        try:
            new_user = client(
                Fname=client_fname,
                Sname=client_sname,
                Email=client_email,
                phone=client_phone,
                date=datetime.datetime.now(),
                password=make_password(client_password),
            )
            new_user.save()
            messages.success(request, 'Registration successful! Welcome to our site.')
            return redirect('login')
        except IntegrityError:
            messages.error(request, ('Email already exists. Please use a different email.'))

    return render(request, 'user/register.html')

def dashboard(request):
    storage = get_messages(request)
    storage.used = True

    user_email = request.session.get('user_email')

    if user_email:
        if client.objects.filter(Email=user_email).exists():

            logged_in_user =client.objects.get(Email=user_email)
            data = {
                'first_name': logged_in_user.Fname,
                'email': logged_in_user.Email,
                'phone': logged_in_user.phone,
                'date': logged_in_user.date,
            }
            return render(request, 'user/home.html', data)
        else:

            messages.error(request, 'User not found.')
            return redirect('login')
    else:
        messages.error(request, 'You are not logged in!')
        return redirect('login')



def logout(request):
    storage = get_messages(request)
    storage.used = True 

    request.session.flush()
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')


def db_queries(request):
    """
    In django table_name.objects.filter() retrieves all records matching the given criteria
    It returns a QuerySet, a list-like containing the elements
    Use filter() when need multiple records
    Doesn't raise errors


    table_name.objects.get() retrieves a single record that mtches the given criteria
    returns a single object instance of the model
    Use get() when need one record at a time
    Raises an error if no record is found, or more than one record matches the criteria

    """
    user_email = request.session.get('user_email')
    client.objects.filter(Email = user_email)

    #get specific data
    row = client.objects.get(Email = user_email)
    password = row.password
    email = row.Email
    date = row.date
    phone = row.phone
    first_name = row.Fname
    second_name = row.Sname
    status = row.status
    balance = f"Ksh {row.Balance}"
    
    #update query works with .filter()
    client.objects.filter(Email = user_email).update(Fname = 'Eunice' ,Sname = "Machora",status ="active")
    #performing operations in update , we use F  to modify a field based on its existing value
    client.objects.filter(Email = user_email).update(Balance = F('Balance') + 50)
    return HttpResponse(balance)