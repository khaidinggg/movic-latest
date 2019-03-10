from django.shortcuts import render,HttpResponse
from .scrap import mainDbpScrape, mainMcpScrape
from django.http import HttpResponse
from .models import PageScrape , DBPScrape, MCPScrape
from movichome import models
import json


def index(request):
    # return HttpResponse('Hello world')
    return render(request, 'home.html')

def about(request):    
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')
    
def result(request):
    #PageScrape.objects.all().delete()
    userinput = request.POST.get('userkeyword', None)
    userkeywords = userinput
    #models.PageScrape.objects.create(title=userkeywords)

    #website satu
    dpbresult = mainDbpScrape.dbp()
    #dpbresult.scrapeItem(userkeywords)

    #website dua
    mcpresult = mainMcpScrape.mcp()
    #mcpresult.scrapeItem(userkeywords)

    item1 = PageScrape.objects.all()
    item2 = DBPScrape.objects.all()
    item3 = MCPScrape.objects.all()

    print(item1.count() , item2.count(), item3.count())


    #currentItem = item1.count()
    currentItem1 = item1.count()
    currentItem2 = item2.count()
    currentItem3 = item3.count()

    return render(request, 'search.html', {'desc1': item1[currentItem1-1], 'desc2': item2[currentItem2-1], 'desc3': item3[currentItem3-1]})
