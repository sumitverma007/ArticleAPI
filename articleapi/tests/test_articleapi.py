import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from articleapi.models import Article

pytestmark = pytest.mark.django_db
@pytest.mark.django_db
class TestArticleApiView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_article_test(self):
        url = reverse("article")
        response = self.client.get(url)

        assert response.json() != None
        assert response.status_code == 200

    def test_unique_article(self):
        
        url = reverse("uniquearticle",kwargs={'pk':1})
        article = mixer.blend(Article)
        response = self.client.get(url)

        assert response.json() != None
        assert response.status_code == 200
        

    def test_post_article_valid(self):
        url = reverse("article")
        input_data =  {
        
        "author_name": "Amit",
        "article_tag": "Crime",
        "article_title": "Something",
        "article_content": "Its also something",
        
        }
        response = self.client.post(url,data = input_data)
        # print(response.status_code)
        assert response.json() != None
        assert response.status_code == 201

    def test_post_article_invalid(self):
        url = reverse("article")
        input_data =  {
        
        "author_name": "Amit",
        "article_tag": "Crime",
        "article_title": "Something",
       
        
        }
        response = self.client.post(url,data = input_data)
        # print(response.status_code)
        assert response.json() != None
        assert response.status_code == 400


    # def test_put_article_valid(self):
    #     url = reverse("article")

