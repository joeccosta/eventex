from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Joe Costa', cpf='12345678901', email='joe.dfq@gmail.com', phone='31-975639338')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
    def test_subscription_email_subject(self):
        expected = 'Confirmação de Inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'contato@eventex.com.br'
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['contato@eventex.com.br', 'joe.dfq@gmail.com']
        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Joe Costa',
            'joe.dfq@gmail.com',
            '12345678901',
            '31-975639338'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
