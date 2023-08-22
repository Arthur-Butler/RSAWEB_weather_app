from django.test import TestCase

from catalog.models import Location
from catalog.models import Weather

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Location.objects.create(location_field="2 Mill Street, Bothasig, Cape Town", long_field="-33.857643", lat_field="18.536426")
        Weather.objects.create(precip_prob_field="0.1", wind_speed_field="38.9", wind_dir_field="NW")

    def test_location_field_max_length(self):
        location = Location.objects.get(id=1)
        max_length = location._meta.get_field('location_field').max_length
        self.assertEqual(max_length, 300)

    def test_lat_field_max_digits(self):
        location = Location.objects.get(id=1)
        max_digits = location._meta.get_field('lat_field').max_digits
        self.assertEqual(max_digits, 20)
    
    def test_long_field_max_digits(self):
        location = Location.objects.get(id=1)
        max_digits = location._meta.get_field('long_field').max_digits
        self.assertEqual(max_digits, 20)
    
    def setUp(self):
        pass

