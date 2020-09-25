from django.db import models
from .validators import validate_file_extension
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from .validators import validate_image_extension

checkAlpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabet characters are allowed.')
checkNRIC = RegexValidator(r'^[0-9A-Z]*$', 'Only NRIC characters are allowed.')

# Create your models here.
#Upload picture here
class File_Meta(models.Model):
    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False,validators=[validate_file_extension])
    score = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now=True)

class Customer_Data(models.Model):
    customerName = models.CharField(max_length=64,validators=[checkAlpha])
    customerAge = models.IntegerField(validators=[MinValueValidator(18)])
    customerDOB = models.DateField()
    serviceOfficerName = models.CharField(max_length=64,validators=[checkAlpha])
    NRIC = models.CharField(max_length=64,validators=[checkAlpha])
    #registrationTime = 
    branchCode= models.IntegerField()
    image = models.FileField(blank=False, null=False,validators=[validate_image_extension])
    #productType 


