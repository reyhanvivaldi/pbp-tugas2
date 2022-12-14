from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data_mywatchlist = MyWatchList.objects.all()

def show_mywatchlist_html(request):
    t, f = 0, 0
    for movie in data_mywatchlist:
        if movie.watched == True:
            t += 1
        else:
            t += 1

    context = {
    'mywatchlist_item': data_mywatchlist,
    'nama': 'Reyhan Vivaldi Adrian',
    'npm': '2106750811',
    'msg': "Selamat! Kamu sudah banyak menonton!" if t>=f else "Wah, kamu masih sedikit menonton!"
}

    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")