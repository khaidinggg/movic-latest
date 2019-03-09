from django.db import models

# Create your models here.
class PageScrape(models.Model):
    text_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    DBPDefinition = models.CharField(max_length = 10000)
    peribahasa = models.CharField(max_length = 2000)
    pantun = models.CharField(max_length = 2000)
    MCPList = models.CharField(max_length = 10000)
    description_2 = models.CharField(max_length = 10000)
    

    def __str__(self):
        return self.title
