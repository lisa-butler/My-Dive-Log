from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_logpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logpage.html')

    def test_get_log_a_dive(self):
        response = self.client.get('/log_a_dive')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logadive.html')

    def test_can_add_item(self):
        response = self.client.post('/log_a_dive', {'date': 'Test Added Item'})
        self.assertRedirects(response, '/')
# failing due to redirect not as expected

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Log Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Log Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_item.html')
