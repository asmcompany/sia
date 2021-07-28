from django.test import TestCase

# user app related import
from django.contrib.auth import get_user_model
from .models import User

# testing authentication
from django.contrib.auth import authenticate, login, logout

# Date & Time
from django.utils.timezone import now

class VEGAN_ACCOUNT_TESTS(TestCase):

    # ========== configs and pre requisites ===========
    
    def setUp(self):
        self.username = "someEmail.as@gmail.com"
        self.password = b"some form ofc0mplexpassword"
        self.name = 'siavash'
        self.User = get_user_model()

    def create_user(self):
        userInstance:User = self.User.objects.create_user(username=self.username, password=self.password)
        return userInstance



    # =========== actual tests =============
    
    def test_create_bulk_accounts(self):
        list_of_created_items = list()
        for i in range(3):
            item = self.User.objects.create_user(username=f'sia{i}@gmail.com', password=str(i*i+12**34), first_name=self.name)
            list_of_created_items.append(item)
        self.assertCountEqual(self.User.objects.all(), list_of_created_items)
        self.assertListEqual(list_of_created_items, list(self.User.objects.all()))

    def test_get_user_model(self):
        self.assertIs(self.User, User)

    def test_user_is_instance_of_user(self):
        userInstance = self.create_user()
        self.assertIsInstance(userInstance, User)
    
    def test_user_creation_naive(self):
        userInstance = self.User(username='self.username', password='self.password')
        userInstance.save()
    
    def test_user_creation_greedy(self):
        userInstance = self.User.objects.create_user(username=self.username, password=self.password)
        userInstance.save()
    
    def test_user_credentials_username(self):
        userInstance = self.create_user()
        self.assertIs(userInstance.username, self.username)

    def test_user_credentials_email(self):
        userInstance = self.create_user()
        self.assertIs(userInstance.email, self.username)

    def test_user_credentials_first_name(self):
        userInstance = self.create_user()
        userInstance.first_name = self.name
        userInstance.save()
        self.assertIs(userInstance.first_name, self.name)

    def test_user_is_staff(self):
        userInstance = self.create_user()
        self.assertFalse(userInstance.is_staff)

    def test_user_is_superuser(self):
        userInstance = self.create_user()
        self.assertFalse(userInstance.is_superuser)

    def test_user_is_active(self):
        userInstance = self.create_user()
        self.assertTrue(userInstance.is_active)

    def test_user_date_joined(self):
        userInstance = self.create_user()
        self.assertGreater(now(), userInstance.date_joined)

    def test_user_not_authenticated(self):
        userInstance = self.create_user()
        self.assertTrue(userInstance.is_authenticated)

