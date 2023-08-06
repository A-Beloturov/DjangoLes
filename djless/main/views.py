from django.shortcuts import render
from django.http import HttpResponse
from .models import Address, Users


def index(request):
    return HttpResponse("<h4>Проверка работы</h4>")


def users(request):
    address = Address()
    user = Users()
    address.address = request.POST.get("address", "Testovaya ul.")
    address.save()
    user.user_address = Address.objects.get(address=address.address)
    user.user_name = request.POST.get("name", "Test")
    user.user_surname = request.POST.get("surname", "Testovich")
    user.user_mail = request.POST.get("mail", "test@test")

    user.save()

    # name = request.POST.get("name", "Test")
    # surname = request.POST.get("surname", "Testovich")
    # age = request.POST.get("age", 29)
    # mail = request.POST.get("mail", "test@test")
    # address = request.POST.get("address", "testovaya ul.")

    return HttpResponse(
        f"<h2>Name: {user.user_name}, Surname: {user.user_surname}, Mail: {user.user_mail}, Address: {address.address}, ID: {user.user_address}</h2>")
# Create your views here.
