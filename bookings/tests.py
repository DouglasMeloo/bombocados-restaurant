from django.test import TestCase
from .models import Reservation, Table, MenuItem


class BookingTestCase(TestCase):

    def setUp(self):
        self.table = Table.objects.create(number=1, size=4)
        self.menu_item = MenuItem.objects.create(name="Pasta", price=12.99)

    def test_table_creation(self):
        self.assertEqual(self.table.number, 1)

    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.name, "Pasta")
        self.assertEqual(self.menu_item.price, 12.99)

    # add more test cases as needed
