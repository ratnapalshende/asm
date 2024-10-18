from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm  # Import to hash passwords
from django.contrib import messages
from .models import UserRegistration

def sign_in(request):
    return render(request, 'client_app/login.html')  # Make sure this path matches your template location

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if UserRegistration.objects.filter(email=email).exists():
                messages.error(request, 'User already exists. Please login or use a different email.')
            else:
                form.save()  # Save the new user
                messages.success(request, 'Registration successful! You can now login.')
                return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()  # Create an empty form for GET request

    # Don't set any messages when rendering the form for the first time
    return render(request, 'client_app/register.html', {'form': form})

    
def registration_success(request):
    return render(request, 'client_app/success.html') 

def subjects(request):
    return render(request, 'client_app/subjects.html')

def pharmacology(request):
    return HttpResponse("Welcome to Pharmacology!")

def pharmaceutical_chemistry(request):
    return HttpResponse("Welcome to Pharmaceutical Chemistry!")

def pharmacognosy(request):
    return HttpResponse("Welcome to Pharmacognosy!")

def pharmaceutics(request):
    return HttpResponse("Welcome to Pharmaceutics!")

def biochemistry(request):
    return HttpResponse("Welcome to Biochemistry!")

def clinical_pharmacy(request):
    return HttpResponse("Welcome to Clinical Pharmacy!")
