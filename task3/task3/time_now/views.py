from django.shortcuts import render

# Create your views here.
def show_time(request):
    return render(request, 'main.html')
