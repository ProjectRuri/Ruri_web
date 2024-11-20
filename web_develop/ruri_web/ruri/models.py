from django.db import models

# Create your models here.

class wav_file(models.Model):
    name = models.CharField(max_length=200)
    content = models.FileField(null=True, upload_to="", blank=True)

    def __str__(self):
        return self.file_name