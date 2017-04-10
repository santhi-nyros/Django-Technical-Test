from django.test import TestCase

# # Create your tests here.
from useraccounts.models import UserProfle
from django.contrib.auth.models import User

class UserProfileModelTest(TestCase):

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

    #Lable testing
    def test_user_label(self):
        user=UserProfle.objects.filter(id=1).first()
        field_label = user._meta.get_field('user').verbose_name
        self.assertEquals(field_label,'user')

    def test_is_user_unique(self):
        user=UserProfle.objects.filter(id=1).first()
        is_user_unique = user._meta.get_field('user').unique
        self.assertTrue(is_user_unique)

    def test_address_label(self):
        user=UserProfle.objects.filter(id=1).first()
        field_label = user._meta.get_field('address').verbose_name
        self.assertEquals(field_label,'address')

    def test_address_max_length(self):
        user=UserProfle.objects.filter(id=1).first()
        max_length = user._meta.get_field('address').max_length
        self.assertEquals(max_length,255)

    def test_address_blank(self):
        user=UserProfle.objects.filter(id=1).first()
        is_user_blank = user._meta.get_field('address').blank
        self.assertTrue(is_user_blank)

    def test_address_default(self):
        user=UserProfle.objects.filter(id=1).first()
        default_val = user._meta.get_field('address').default
        self.assertEquals(default_val,"")




class UserModelTest(TestCase):

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

    #Lable testing
    def test_username_label(self):
        user=User.objects.filter(id=1).first()
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_first_name_label(self):
        user=User.objects.filter(id=1).first()
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_last_name_label(self):
        user=User.objects.filter(id=1).first()
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_password_label(self):
        user=User.objects.filter(id=1).first()
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label,'password')


    # Field length checking start
    def test_username_max_length(self):
        user=User.objects.filter(id=1).first()
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length,150)

    def test_first_name_max_length(self):
        user=User.objects.filter(id=1).first()
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length,30)

    def test_last_name_max_length(self):
        user=User.objects.filter(id=1).first()
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length,30)

    def test_email_max_length(self):
        user=User.objects.filter(id=1).first()
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length,254)

    def test_password_max_length(self):
        user=User.objects.filter(id=1).first()
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length,128)


    # Checking model returns object
    def test_object_name_is_username(self):
        user=User.objects.filter(id=1).first()
        expected_object_name = '%s' % (user)
        self.assertEquals(expected_object_name,str(user))



