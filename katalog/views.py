from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

# ambil dari models, karena perlu akses ke database
data_katalog = CatalogItem.objects.all()

# untuk dipanggil di template (html)
context = {
    'katalog_item': data_katalog,
    'nama': 'Reyhan Vivaldi Adrian',
    'npm': '2106750811'
}

def show_katalog(req):
    return render(req, "katalog.html", context)   # render itu ngapain? biar masuk ke urls?