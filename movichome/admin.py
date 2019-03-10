from django.contrib import admin
from .models import PageScrape, MCPScrape, DBPScrape

# Register your models here.

class MCPAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Test', {'fields': ['MCPList'], 'classes': ['collapse']}),
        ('Test', {'fields': ['description_2'], 'classes': ['collapse']}),
        ('Test', {'fields': ['pub_date_mcp'], 'classes': ['collapse']}),
    ]

    list_display = ('MCPList', 'title',  'description_2', 'pub_date_mcp')
#    field = ['MCPList', 'title',  'description_2', 'pub_date_mcp']


class DBPAdmin(admin.ModelAdmin):
    #model = DBPScrape

    fieldsets = [
        (None,               {'fields': ['title']}),
#        ('Test', {'fields': ['text_id'], 'classes': ['collapse']}),
        ('Test', {'fields': ['DBPDefinition'], 'classes': ['collapse']}),
        ('Test', {'fields': ['peribahasa'], 'classes': ['collapse']}),
        ('Test', {'fields': ['pantun'], 'classes': ['collapse']}),
    ]

    list_display = ('title', 'DBPDefinition', 'peribahasa', 'pantun')
#    field = ['title', 'DBPDefinition', 'peribahasa', 'pantun']





class ScrapeAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['title']}),
#        ('Test', {'fields': ['text_id'], 'classes': ['collapse']}),
#        ('Test', {'fields': ['DBPDefinition'], 'classes': ['collapse']}),
#        ('Test', {'fields': ['peribahasa'], 'classes': ['collapse']}),
#        ('Test', {'fields': ['pantun'], 'classes': ['collapse']}),
#    ]

#    list_display = ('text_id', 'title', 'DBPDefinition', 'peribahasa', 'pantun')
    field = ['text_id', 'title']
    #inlines = [DBPAdmin]
    #inlines = [MCPAdmin]


#admin.site.register(PageScrape, ScrapeAdmin)
admin.site.register(PageScrape, ScrapeAdmin)
admin.site.register(MCPScrape, MCPAdmin)
admin.site.register(DBPScrape, DBPAdmin)
