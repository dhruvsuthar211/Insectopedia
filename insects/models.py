from django.db import models

class ContentOrder(models.Model):
    name = models.CharField(unique=True, max_length=100)
    common_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'content_order'

    def __str__(self):
        return self.name

class ContentFamily(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    order = models.ForeignKey(ContentOrder, on_delete=models.CASCADE)
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'content_family'

    def __str__(self):
        return self.name

class ContentSpecies(models.Model):
    scientific_name = models.CharField(unique=True, max_length=150)
    common_name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    diet = models.TextField()
    lifespan = models.TextField()
    conservation_status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    geographical_scope = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='', max_length=500)
    slug = models.CharField(unique=True, max_length=150)
    family = models.ForeignKey(ContentFamily, on_delete=models.CASCADE)
    habitat = models.TextField()

    class Meta:
        managed = True
        db_table = 'content_species'

    def __str__(self):
        return self.scientific_name