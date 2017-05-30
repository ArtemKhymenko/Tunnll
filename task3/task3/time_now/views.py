from django.shortcuts import render
import datetime

# Create your views here.
def show_time(request):
    now = datetime.datetime.now()
    return render(request, 'main.html', {'now':now})
