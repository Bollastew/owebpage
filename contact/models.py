import uuid

from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


class WebPageOwnerInfo(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    owner_name = models.CharField(max_length=30, help_text='Enter owner of webpage')
    owner_twitter = models.CharField(max_length=40, help_text='Enter twitter url')
    owner_description = models.CharField(max_length=400, help_text='Enter small description of yourself')
    ...

    # Metadata
    class Meta:
        ordering = ['-owner_name', 'owner_twitter', 'owner_description']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def get_owner_name(self):
        return self.owner_name

    def get_owner_twitter(self):
        return self.owner_twitter

    def get_owner_description(self):
        return self.owner_description

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.owner_name}, {self.owner_twitter}'