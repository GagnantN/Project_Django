import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    data_dict = {
        "links": [
            {"url": "/", "title": "Accueil"},
        ],
        "root_dir": ""
    }
    context = {'data_dict' : data_dict}
    return render(request, 'index.html', context)

def list(request):
    data_dict = {
        "links": [
            {"url": "/", "title": "Accueil"},
            {"url": "/list/", "title": "Photo de Fantasy"},
        ],
        # "current": "Page Coucou",
        "root_dir": ""
    }

    
    # Liste des images dans le dossier 'data'
    images_folder = os.path.join(settings.BASE_DIR, 'data')
    images = []
    for filename in os.listdir(images_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images.append(filename)


    context = {
        'data_dict': data_dict,
        'images' : images
        }
    return render(request, 'list.html', context)