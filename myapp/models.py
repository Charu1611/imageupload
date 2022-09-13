from django.db import models  
  
class UploadImage(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    user=models.CharField(max_length=30,default='myname',null=True)
    def __str__(self):
        return self.caption