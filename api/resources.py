from tastypie.resources import ModelResource
from movichome.models import PageScrape
class ScrapResource(ModelResource):
    class Meta:
        queryset = PageScrape.objects.all()
        resource_name = 'scrap'
