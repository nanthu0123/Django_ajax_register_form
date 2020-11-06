from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import UserRegister


def index(request):
    return render(request, 'index.html')


def create_user(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        date = request.POST['datefilter']

        print(name, email, password)

        UserRegister.objects.create(
            Name=name,
            Email=email,
            Password=password,
            Date=date
        )
    return redirect('index')


def view_user(request):

    if request.method == 'POST':
        try:
            name = request.POST['search']
            users = UserRegister.objects.get(Name=name)
            return render(request, 'profile.html', {'user': users})

        except ObjectDoesNotExist:
            messages.error(request, 'user data does not exist')

    if request.method == 'GET':
        if 'term' in request.GET:
            qs = UserRegister.objects.filter(
                Name__istartswith=request.GET.get('term'))
            names = []
            for User in qs:
                names.append(User.Name)
            return JsonResponse(names, safe=False)

    return render(request, 'profile.html')
