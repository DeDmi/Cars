from django.db import models

# Create your models here.


class Cars(models.Model):
    title = models.CharField(max_length=500)
    year_c = models.CharField(max_length=500)
    links_c = models.CharField(max_length=500)
    price_USE_c = models.CharField(max_length=500)
    price_UA_c = models.CharField(max_length=500)
    city_c = models.CharField(max_length=500)
    #photo = models.ImageField(upload_to='photos%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


