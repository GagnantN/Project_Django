import os
from django.conf import settings
from django.shortcuts import render

def render_page(request, template_name, breadcrumb_links, current_page="", images_folder=None):
    data_dict = {
        "links": breadcrumb_links,
        "current": current_page,
        "root_dir": ""
    }
    
    images = []
    if images_folder:
        folder_path = os.path.join(settings.BASE_DIR, images_folder)
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(filename)
    
    context = {
        'data_dict': data_dict,
        'images': images
    }
    return render(request, template_name, context)


def index(request):
    links = [{"url": "/", "title": "Accueil"}]
    return render_page(request, 'index.html', links)

def list(request):
    links = [
        {"url": "/", "title": "Accueil"},
        {"url": "/list/", "title": "Photo de Fantasy"}
    ]
    return render_page(request, 'list.html', links, images_folder="data")

def carde(request):
    # Récupère la valeur après ?img=
    image_selected = request.GET.get('img')  

    data_dict = {
        "links": [
            {"url": "/", "title": "Accueil"},
            {"url": "/list/", "title": "Photo de Fantasy"},
        ],
        "current": "Carde",
        "root_dir": ""
    }

    context = {
        'data_dict': data_dict,
        'image': image_selected
    }
    return render(request, 'carde.html', context)
