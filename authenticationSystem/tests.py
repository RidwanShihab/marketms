from django.test import TestCase
# Create your tests here.
from django.urls import resolve, reverse
from django.contrib.auth.models import User

from authenticationSystem.models import *

class userTestCase(TestCase):

    def setUp(self):
        u = User.objects.create(username="kabir", password="kabir")
        bill.objects.create(biller=u, method="Nagad", tid="0121", amount="4000", month="march,2020")



    def test_bill(self):
       l = User.objects.get(username="kabir")
       self.assertEqual(l.username, "kabir")


class urlTestCase(TestCase):
    def test_URL(self):

        """Animals that can speak are correctly identified"""
        url = reverse('billingpage')
        print(resolve(url))
        url = reverse('signuppage')
        print(resolve(url))
        url = reverse('profilepage')
        print(resolve(url))
        url = reverse('applyshoppage')
        print(resolve(url))


class profileTestCase(TestCase):

    def setUp(self):
        u = User.objects.create(username="abir", password="abir")
        v=bill.objects.create(biller=u, method="Nagad", tid="0121", amount="4000", month="march,2020")



    def test_bill(self):
       v = bill.objects.get(tid="0121")
       self.assertEqual(v.amount, "4000")

