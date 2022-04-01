from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            rec = Customer(name=request.user.get_username())
            rec.save()
            return redirect('view_items')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_items')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


#def home_view(request):
   # user = Customer.objects.all()
   # return render(request, 'home.html', {'users': user})


#class CustomerView(viewsets.ModelViewSet):
    #queryset = Customer.objects.all()
    #serializer_class = CustomerSerializer


#@api_view(['POST'])
#def add_items(request):
    #cust = CustomerSerializer(data=request.data)

    #if Customer.objects.filter(**request.data).exists():
        #raise serializers.ValidationError('This data already exists')

    #if cust.is_valid():
        #cust.save()
        #return Response(cust.data)
   # else:
       # return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):

    if request.query_params:
        cust = Customer.objects.filter(**request.query_param.dict())
    else:
        cust = Customer.objects.all()

    if cust:
        serializer = CustomerSerializer(cust, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    cust = Customer.objects.get(pk=pk)
    data = CustomerSerializer(instance=cust, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
    cust = Customer.objects.get(id=pk)
    cust.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


