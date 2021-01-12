from django.db import models
from django.forms import ModelForm,TextInput,EmailInput
# Create your models here.

class setting(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=250)
    description = models.CharField(max_length=350)
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True, max_length=200)
    phone = models.CharField(blank=True, max_length=50)
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, max_length=50)
    smatpserver = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=50)
    smtpport = models.CharField(blank=True, max_length=5)
    logo = models.ImageField(blank = True, upload_to = 'images/')
    facebook = models.CharField(blank=True, max_length=50)
    Instragram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    refarence = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class ContactMassage(models.Model):
    
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    subject = models.CharField( max_length=100)
    massage = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=50, choices=STATUS,default='New' )
    ip = models.CharField(max_length=100, blank=True, )
    Note = models.CharField(max_length=200, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMassage
        fields = ['name', 'email', 'massage']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder':'Name please'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder':'email please'}),
            'massage': TextInput(attrs={'class': 'input', 'placeholder':'Give massage'}),
        }