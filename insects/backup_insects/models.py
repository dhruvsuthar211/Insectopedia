from django.db import models

class Insect(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.CharField(max_length=100) # e.g., Lepidoptera
    family = models.CharField(max_length=100)
    image = models.ImageField(upload_to='insects/', null=True, blank=True)

    def __str__(self):
        return self.common_name