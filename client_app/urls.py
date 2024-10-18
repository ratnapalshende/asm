from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.sign_in, name='login'), 
    path('login/', views.sign_in, name='login'),  # Route for the sign-in page
    path('register/', views.register_view, name='register'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('subjects/', views.subjects, name='subjects'),
    path('sub1/', views.pharmacology, name='pharmacology'),
    path('sub2/', views.pharmaceutical_chemistry, name='pharmaceutical_chemistry'),
    path('sub3/', views.pharmacognosy, name='pharmacognosy'),
    path('sub4/', views.pharmaceutics, name='pharmaceutics'),
    path('sub5/', views.biochemistry, name='biochemistry'),
    path('sub6/', views.clinical_pharmacy, name='clinical_pharmacy'),
]
