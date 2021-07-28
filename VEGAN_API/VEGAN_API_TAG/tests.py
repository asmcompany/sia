from django.test import TestCase

from .models import TAG
class TestTag(TestCase):

    def setUp(self):
        self.instance = TAG()
        self.title = 'vegi corp'

    def test_create(self):
        instance =  self.instance
        instance.title = 'vegi corp'
        instance.save()

        self.assertEqual(instance.title, self.title)

    def test_slug(self):
        instance = TAG.objects.create(title=self.title)
        self.assertEqual(TAG.objects.count(), 1)
        self.assertEqual(instance.slug, self.title.replace(' ', '-'))
