from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Photo(models.Model):
    type_of_pic = models.ForeignKey(Type, on_delete=models.CASCADE)
    visible_to_public = models.BooleanField(default=True)
    name = models.CharField(max_length=200, null=True, blank=False)
    pic_url = models.CharField(max_length=800, null=True, blank=True)

    def __str__(self):
        return self.name


