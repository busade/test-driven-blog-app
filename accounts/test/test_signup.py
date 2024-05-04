from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegistrationForm
from django.contrib.auth import get_user_model
# Create your tests here.




class AccountCreationTest(TestCase):
    def setUp (self) -> None:

        self.form_class = UserRegistrationForm
        


    def test_signup_page_exist(self):
        response = self.client.get(reverse('signup_page'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, "Create your account today")



    def test_signup_form_works(self):

        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields ),
        self.assertTrue('username' in self.form_class.Meta.fields )
        self.assertTrue('password1' in self.form_class.Meta.fields )
        self.assertTrue('password2' in self.form_class.Meta.fields )

        sample_data = {
            "email": "testuser@app.com",
            "username":"testuser",
            "password1": "Password#@",
            "password2": "Password#@"
        }
        form = self.form_class(sample_data)
        self.assertTrue(form.is_valid())




    def test_signup_form_creates_user_in_db(self):

        user = {
            "email": "testuser3@app.com",
            'username': "usernme",
            "password1": "Password#@",
            "password2": "Password#@"
        }

        form = self.form_class(user)
        User = get_user_model()
        if form.is_valid():
           form.save()      
        self.assertEqual(User.objects.count(),1)
