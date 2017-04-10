from django.test import TestCase
from django.contrib.auth.models import User
from useraccounts.models import UserProfle
# # Create your tests here.

class LoginTestClass(TestCase):

    def setUp(self):
        self.user = User()
        self.user.username = 'username'
        self.user.first_name = 'f_name'
        self.user.last_name = 'l_name'
        self.user.email = 'sample@yopmail.com'
        self.user.set_password('password')
        self.user.save()
        self.uprof = UserProfle()
        self.uprof.user = self.user
        self.uprof.address = 'address'
        self.uprof.save()

    def test_home_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_login_with_get_method(self):
        #Get method
        resp = self.client.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)

    def test_login_with_post_method(self):
        resp = self.client.post('/accounts/login/',{'email':'sample@yopmail.com', 'password':'password'})
        self.assertEqual(resp.status_code, 302)

    def test_user_reg_page_get_method(self):
        resp = self.client.get('/accounts/reg/')
        self.assertEqual(resp.status_code, 200)

    def test_user_reg_page_post_method(self):
        data={
                'username':'tester1',
                'first_name':"first_name",
                'last_name':'last_name',
                'email':'tester@yopmail.com',
                'password':'password',
                'address':'address'
            }
        resp = self.client.post('/accounts/reg/', data)
        self.assertEqual(resp.status_code, 200)

    def test_logout(self):
        resp = self.client.get('/accounts/logout/')
        self.assertEqual(resp.status_code, 302)

    def test_updateprofile_page_with_get_method(self):
        resp = self.client.login(username='username', password='password')
        self.assertTrue(resp)
        resp = self.client.get('/accounts/update/')
        self.assertEqual(resp.status_code, 200)

    def test_updateprofile_page_with_post_method(self):
        resp = self.client.login(username='username', password='password')
        self.assertTrue(resp)
        data = {'username':'username','first_name':'first_name','last_name':'last_name','address':'address'}
        resp = self.client.post('/accounts/update/', data)
        self.assertEqual(resp.status_code,302)

    def test_changepassword_page_with_get_method(self):
        resp = self.client.login(username='username', password='password')
        self.assertTrue(resp)
        resp = self.client.get('/accounts/reset_password/')
        self.assertEqual(resp.status_code, 200)

    def test_changepassword_page_with_post_method(self):
        resp = self.client.login(username='username', password='password')
        self.assertTrue(resp)
        data = {'password':'password','password_confirm':'password_confirm'}
        resp = self.client.get('/accounts/reset_password/', data)
        self.assertEqual(resp.status_code, 200)

