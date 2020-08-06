from django.db import models
from .validators import validate_file_extension

# Create your models here.
class File_Meta(models.Model):
    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False,validators=[validate_file_extension])
    score = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now=True)