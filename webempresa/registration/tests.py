from django.test import TestCase

from django.contrib.auth.models import User
from registration.models import Profile
# Create your tests here.

class ProfileTestCase(TestCase):
    '''clase con métodos para preparar y probar la prueba unitaria'''
    def setUp(self):
        # preparar la prueba
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        # probar la prueba
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)