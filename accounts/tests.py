from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
# Create your tests here.




class AccountCreationTest(TestCase):
    def test_signup_page_exist(self):
        response = self.client.get(reverse('signup_page'))
        self.assertEqual(response, HTTPStatus.OK)
        self.assertTemplateUsed()