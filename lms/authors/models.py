from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    # class Meta:
    #     table_name = "authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
