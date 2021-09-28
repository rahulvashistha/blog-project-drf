from crispy_forms.layout import Row
from django.db import models

# Create your models here.
# Contact model for the user.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name + ' - ' + self.email