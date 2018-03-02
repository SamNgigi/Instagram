from django.shortcuts import render
from .models import Image
# Create your views here.


def home(request):
    test = 'Working'
    image_test = Image.objects.all()
    content = {
        "test": test,
        "image_test": image_test
    }
    return render(request, 'index.html', content)
