from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_item_string_method_returns_date(self):
        item = Item.objects.create(name='Test_Log_Item')
        self.assertEqual(str(item), 'Test_Log_Item')
