from django.test import TestCase, Client
from django.urls import resolve, reverse
from mywatchlist.views import show_mywatchlist_html, show_mywatchlist_json, show_mywatchlist_xml

client = Client()

# Create your tests here.
class TestApp(TestCase):
    def test_app_html_exists(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def test_app_json_exists(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    
    def test_app_xml_exists(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)