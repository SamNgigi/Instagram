from django.shortcuts import render

# Create your views here.


def home(request):
    test = 'Working'
    content = {
        "test": test,
    }
    return render(request, 'index.html', content)
