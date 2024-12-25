from django.shortcuts import render


def canny(request):
    return render(request, 'filter/canny.html')
