from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data_mywatchlist = MyWatchList.objects.all()

context = {
    'mywatchlist_item': data_mywatchlist,
    'nama': 'Reyhan Vivaldi',
    'npm': '2106750811'
}

def show_mywatchlist_html(request):
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")