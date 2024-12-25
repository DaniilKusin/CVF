from django.shortcuts import render


def filters_page(request):
    return render(request, 'main/filters_page.html')
