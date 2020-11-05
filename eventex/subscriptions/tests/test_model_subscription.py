from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Joe Campos Costa',
            cpf='01234567890',
            email='joe.dfq@gmail.com',
            phone='31-975639338'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """ Subscription must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Joe Campos Costa', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)