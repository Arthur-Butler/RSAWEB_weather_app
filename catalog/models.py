import uuid
from django.db import models
from django.urls import reverse

class Location(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    location_field = models.CharField(max_length=300, help_text='Enter your location')
    long_field=models.DecimalField(default=0.0, max_digits=20, decimal_places=10)
    lat_field=models.DecimalField(default=0.0, max_digits=20, decimal_places=10)
    # …

    # Metadata
    class Meta:
        ordering = ['-location_field']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.location_field
    
class Weather(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    precip_prob_field = models.CharField(max_length=10)
    wind_speed_field = models.CharField(max_length=10)
    wind_dir_field = models.CharField(max_length=10)
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    # …

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('weather-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.location_field

