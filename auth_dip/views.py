from django.shortcuts import render, redirect
from .forms import AuthDbForm
from .models import AuthDb
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.


def auth_dip_index(request):
    error = ''
    # data = {}

    try:
        if request.session['user'] is not None and request.session['admin'] is True:
            if request.method == "POST" and request.POST['Logout']:
                del request.session['user']
                del request.session['admin']
            return redirect('http://127.0.0.1:8000/admin-profile/')
        elif request.session['user'] is not None and request.session['admin'] is False:
            if request.method == "POST" and request.POST['Logout']:
                del request.session['user']
                del request.session['admin']
            return redirect('http://127.0.0.1:8000/catalog/')
    except KeyError:
        if request.method == "POST":
            form = AuthDbForm(request.POST)
            if form.is_valid():
                cleaned_info = form.cleaned_data
                if AuthDb.objects.filter(
                        Q(Login=cleaned_info['Login']) & Q(Password=cleaned_info['Password']) & Q(IsAdmin=False)).all():
                    request.session['user'] = cleaned_info['Login']
                    request.session['admin'] = False
                    return redirect('http://127.0.0.1:8000/catalog/')
                elif AuthDb.objects.filter(
                        Q(Login=cleaned_info['Login']) & Q(Password=cleaned_info['Password']) & Q(IsAdmin=True)).all():
                    request.session['user'] = cleaned_info['Login']
                    request.session['admin'] = True
                    return redirect('http://127.0.0.1:8000/admin-profile/')
                else:
                    error = "Login or Password was incorrect!"
            else:
                return redirect('http://127.0.0.1:8000/')

        form = AuthDbForm()

        data = {
            'form': form,
            'error': error
        }

        return render(request, 'auth_dip/auth_index.html', data)