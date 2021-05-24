from django.shortcuts import render

# Create your views here.


def admin_profile_index(request):
    return render(request, 'admin_profile/admin_index.html')
