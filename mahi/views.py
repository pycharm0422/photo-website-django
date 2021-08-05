from django.shortcuts import render
from .models import Photo, Type


def home(request):
    photos = Photo.objects.filter(visible_to_public=True)
    Types = Type.objects.all()
    context = {
        "photos":photos,
        "types":Types,
    }
    return render(request, 'mahi/home.html', context)


def filterPage(request, type_of_pic):
    photos = Photo.objects.filter(type_of_pic__name=type_of_pic)
    Types = Type.objects.all()

    context = {
        "type_of_pic":type_of_pic,
        "photos":photos,
        "types":Types,

    }
    return render(request, 'mahi/filterPics.html', context)
def aboutMe(request):
    return render(request, 'mahi/about.html')

def contactPage(request):
    return render(request, 'mahi/contact.html')