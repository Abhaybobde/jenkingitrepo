from django.shortcuts import render
from credit.models import PlatinumModel,goldModel,silverModel
# Create your views here.
def platinum_list_view(r):
    objects = PlatinumModel.objects.all()  # ORM query
    my_dict = {'objects': objects}
    return render(r,'list_request/platinum_list.html',context=my_dict)

def gold_list_view(r):
    objects = goldModel.objects.all()  # ORM query
    my_dict = {'objects': objects}
    return render(r,'list_request/gold_list.html',context=my_dict)
def silver_list_view(r):
    objects = silverModel.objects.all()  # ORM query
    my_dict = {'objects': objects}
    return render(r,'list_request/silver_list.html',context=my_dict)