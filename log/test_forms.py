from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    def test_item_date_is_required(self):
        form = ItemForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_item_location_is_required(self):
        form = ItemForm({'location': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('location', form.errors.keys())
        self.assertEqual(form.errors['location'][0], 'This field is required.')

    def test_item_depth_is_required(self):
        form = ItemForm({'depth': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('depth', form.errors.keys())
        self.assertEqual(form.errors['depth'][0], 'This field is required.')

    def test_item_time_is_required(self):
        form = ItemForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_item_buddy_is_required(self):
        form = ItemForm({'buddy': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('buddy', form.errors.keys())
        self.assertEqual(form.errors['buddy'][0], 'This field is required.')              

    def test_item_note_field_is_not_required(self):
        form = ItemForm({'note': 'Test note'})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['date', 'location', 'depth', 'time', 'buddy', 'note'])