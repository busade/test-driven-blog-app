from django.test import TestCase
from ..models import Post
from http import HTTPStatus
from model_bakery import baker

# Create your tests here.



class Homepage(TestCase):
    def setUp(self) -> None:
        self.post1 = baker.make(Post)
        self.post2 = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post1.title)
        self.assertContains(response,self.post2.title)



