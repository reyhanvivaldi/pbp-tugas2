from django.urls import path
from mywatchlist.views import show_mywatchlist_json
from mywatchlist.views import show_mywatchlist_xml
from mywatchlist.views import show_mywatchlist_html

app_name = 'mywatchlist'

urlpatterns = [
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
]