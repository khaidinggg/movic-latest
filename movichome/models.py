from django.db import models


# Create your models here.
class PageScrape(models.Model):
    text_id = models.AutoField(primary_key=True)
    #pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title

class DBPScrape(models.Model):
    #DBP2 = models.ForeignKey(PageScrape, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    DBPDefinition = models.CharField(max_length = 10000)
    peribahasa = models.CharField(max_length = 2000)
    pantun = models.CharField(max_length = 2000)
    pub_date_dbp = models.CharField(max_length = 100)

    def __str__(self):
        return self.title


class MCPScrape(models.Model):
    #MCP2 = models.ForeignKey(PageScrape, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    MCPList = models.CharField(max_length = 10000)
    description_2 = models.CharField(max_length = 10000)
    #pub_date_mcp = models.DateTimeField('date published')
    pub_date_mcp = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title
