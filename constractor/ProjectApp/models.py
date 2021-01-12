from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class ConstractionCatagory(models.Model):
    status =(
        ('True', 'True'),
        ('False', 'False'),
    )
    
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=250)
    image = models.ImageField(blank = True, upload_to = 'catagory/')
    details = models.TextField()
    status = models.CharField(max_length=10, choices=status)
    slug = models.SlugField(null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class ConstractionProject(models.Model):
    status =(
        ('True', 'True'),
        ('False', 'False'),
    )
    catagory = models.ForeignKey(ConstractionCatagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=250)
    image = models.ImageField(blank = True, upload_to = 'products/',null= True)
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    details = models.TextField()
    status = models.CharField(max_length=10, choices=status)
    slug = models.SlugField(null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def imageurl(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
       
        return "#"

    def image_tag(self):
        return mark_safe('<img src="{}" width="120" height="70" />'.format(self.image.url))
    image_tag.short_description = "Image"
    

    