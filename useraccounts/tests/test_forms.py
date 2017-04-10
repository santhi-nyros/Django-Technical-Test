from django.test import TestCase

# # Create your tests here.
import datetime
from django.utils import timezone
from useraccounts.forms import RegistrationForm, LoginForm, EditForm, PasswordResetForm, ForgotPasswordForm

class RegistrationFormTest(TestCase):
    #Checking form labels
    def test_form_labels(self):
        form = RegistrationForm()
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'Username')
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'First name')
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Last name')
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Email')
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Password')
        self.assertTrue(form.fields['address'].label == None or form.fields['address'].label == 'Address')


    #Checking form error messages
    def test_form_fields_error_messages(self):
        form = RegistrationForm()
        self.assertEqual(form.fields['username'].required,True)
        self.assertEqual(form.fields['first_name'].required,True)
        self.assertEqual(form.fields['last_name'].required,False)
        self.assertEqual(form.fields['email'].required,True)
        self.assertEqual(form.fields['password'].required,True)
        self.assertEqual(form.fields['address'].required,False)


    def test_form_fields_max_length(self):
        form = RegistrationForm()
        self.assertEqual(form.fields['username'].max_length,50)
        self.assertEqual(form.fields['first_name'].max_length,140)
        self.assertEqual(form.fields['last_name'].max_length,140)
        self.assertEqual(form.fields['email'].max_length,50)
        self.assertEqual(form.fields['address'].max_length,250)

    #Checking form data validations
    def test_form_data_validations(self):
        form_data = {'username': 'stest', 'first_name': 'sandy', 'last_name': 'test', 'email': 'sample@yopmail.com','password': '123456','address': 'address'}
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())



class LoginFormTest(TestCase):
    #Checking form labels
    def test_form_labels(self):
        form = LoginForm()
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Email')
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Password')

    #Checking form error messages
    def test_form_fields_error_messages(self):
        form = LoginForm()
        self.assertEqual(form.fields['email'].required,True)
        self.assertEqual(form.fields['password'].required,True)

    #Checking form fileds max length
    def test_form_fields_max_length(self):
        form = RegistrationForm()
        self.assertEqual(form.fields['email'].max_length,50)

    #Checking form data validations
    def test_form_data_validations(self):
        form_data = {'email': 'sample@yopmail.com', 'password': '123456'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_data = {'email': 'sampleyopmail.com', 'password': '123456'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())


class EditFormTest(TestCase):
    #Checking form labels
    def test_form_labels(self):
        form = EditForm()
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'Username')
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'First name')
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Last name')
        self.assertTrue(form.fields['address'].label == None or form.fields['address'].label == 'Address')

    #Checking form error messages
    def test_form_fields_error_messages(self):
        form = EditForm()
        self.assertEqual(form.fields['username'].required,True)
        self.assertEqual(form.fields['first_name'].required,True)
        self.assertEqual(form.fields['last_name'].required,False)
        self.assertEqual(form.fields['address'].required,False)

    def test_form_fields_max_length(self):
        form = EditForm()
        self.assertEqual(form.fields['username'].max_length,50)
        self.assertEqual(form.fields['first_name'].max_length,140)
        self.assertEqual(form.fields['last_name'].max_length,140)
        self.assertEqual(form.fields['address'].max_length,250)


    #Checking form data validations
    def test_form_data_validations(self):
        form_data = {'username': 'stest', 'first_name': 'sandy', 'last_name': 'test', 'address':'address'}
        form = EditForm(data=form_data)
        self.assertTrue(form.is_valid())




class PasswordResetFormTest(TestCase):
    #Checking form labels
    def test_form_labels(self):
        form = PasswordResetForm()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Password')
        self.assertTrue(form.fields['password_confirm'].label == None or form.fields['password_confirm'].label == 'Confirm Password')

    #Checking form error messages
    def test_form_fields_error_messages(self):
        form = PasswordResetForm()
        self.assertEqual(form.fields['password'].required,True)
        self.assertEqual(form.fields['password_confirm'].required,True)

    #Checking form data validations
    def test_form_data_validations(self):
        form_data = {'password': 'password', 'password_confirm': 'password'}
        form = PasswordResetForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_data = {'password': 'password123', 'password_confirm': ''}
        form = PasswordResetForm(data=form_data)
        self.assertFalse(form.is_valid())


class ForgotPasswordFormTest(TestCase):

    def test_form_labels(self):
        form = ForgotPasswordForm()
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Email')
    #Checking form error messages
    def test_form_fields_error_messages(self):
        form = ForgotPasswordForm()
        self.assertEqual(form.fields['email'].required,True)

    #Checking form fileds max length
    def test_form_fields_max_length(self):
        form = ForgotPasswordForm()
        self.assertEqual(form.fields['email'].max_length,50)

    #Checking form data validations
    def test_form_data_validations(self):
        form_data = {'email': 'sample@yopmail.com'}
        form = ForgotPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_data = {'email': 'sampleyopmail.com'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

