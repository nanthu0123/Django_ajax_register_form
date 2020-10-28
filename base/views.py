from django.shortcuts import redirect, render
from .models import UserRegister


def index(request):
    return render(request, 'index.html')


def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        print(name, email, password)

        UserRegister.objects.create(
            Name=name,
            Email=email,
            Password=password
        )

    return redirect('index')
