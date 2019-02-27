from django.db import models


class File(models.Model ):
    file_name = models.CharField(("Nome"), max_length=50)
    upload_data = models.DateField()
    file_data = models.FileField(upload_to="static/files/", null=True,blank=True)  

    def __str__(self):
        return "teste"

