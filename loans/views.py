from django.shortcuts import render

# Create your views here.
def personal_view(r):
    return  render(r, "loans/personal.html")
def car_view(r):
    return render(r,"loans/car.html")
def bussiness_view(r):
    return render(r,"loans/bussiness.html")
def home_view(r):
    return render(r, "loans/home.html")