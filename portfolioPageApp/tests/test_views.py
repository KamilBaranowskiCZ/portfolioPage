import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_main_view(client):
   url = reverse('mainPage')
   response = client.get(url)
   assert response.status_code == 200

def test_CV_view(client):
   url = reverse('CVPage')
   response = client.get(url)
   assert response.status_code == 200

def test_contactPage_view(client):
   url = reverse('contactPage')
   response = client.get(url)
   assert response.status_code == 200

def test_aboutmePage_view(client):
   url = reverse('aboutmePage')
   response = client.get(url)
   assert response.status_code == 200

def test_footballPage_view(client):
   url = reverse('footballPage')
   response = client.get(url)
   assert response.status_code == 200

def test_roomPage_view(client):
   url = reverse('roomPage')
   response = client.get(url)
   assert response.status_code == 200

def test_citation_view(client):
   url = reverse('citation')
   response = client.get(url)
   assert response.status_code == 200

def test_portfolio_view(client):
   url = reverse('portfolio')
   response = client.get(url)
   assert response.status_code == 200

def test_rockpaperscissors_view(client):
   url = reverse('rockpaperscissors')
   response = client.get(url)
   assert response.status_code == 200