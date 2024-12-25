from django.shortcuts import render


def gaussian_blur(request):
    return render(request, 'filter/gaussian_blur.html')
