from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Joe Campos Costa',
            cpf='012345678901',
            email='joe.dfq@gmail.com',
            phone='31-975639338'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """ Subscription must have an auto created at attr."""
        self.assertIsInstance(self.obj.create_at, datetime)
