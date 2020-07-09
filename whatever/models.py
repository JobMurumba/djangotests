from django.db import models

# Create your models here.



class Whatever(models.Model):
    name=models.CharField(max_length=50)
    body=models.TextField()
    creatd_at=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
