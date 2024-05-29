from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
       Menu.objects.create(title="Banana shake", price=10, inventory=20)
       Menu.objects.create(title="Peanut butter shake", price=12, inventory=20)
       Menu.objects.create(title="Smoothie", price=6.77, inventory=20)
       Menu.objects.create(title="Milkshake", price=4.5, inventory=20)
       
    
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 4)
        
        expected_values = [
            "Banana shake : 10.00",
            "Peanut butter shake : 12.00",
            "Smoothie : 6.77",
            "Milkshake : 4.50",
        ]
        
        item_list = [f"{item.title} : {str(item.price)}" for item in items]
        
        self.assertListEqual(item_list, expected_values)
        self.assertIs
        
        