from django.shortcuts import render


def binarization_page(request):
    return render(request, 'filter/binarization.html')
