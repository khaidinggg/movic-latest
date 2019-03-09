from django.contrib import admin
from .models import PageScrape

# Register your models here.

class ScrapeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text_id']}),
        (None,               {'fields': ['title']}),
        ('Test', {'fields': ['DBPDefinition'], 'classes': ['collapse']}),
        ('Test', {'fields': ['peribahasa'], 'classes': ['collapse']}),
        ('Test', {'fields': ['pantun'], 'classes': ['collapse']}),
        ('Test', {'fields': ['MCPList'], 'classes': ['collapse']}),
        ('Test', {'fields': ['description_2'], 'classes': ['collapse']}),
    ]
    
    list_display = ('text_id', 'title', 'DBPDefinition', 'peribahasa', 'pantun', 'MCPList', 'description_2')



admin.site.register(PageScrape, ScrapeAdmin)
