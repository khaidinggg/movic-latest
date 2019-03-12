"""movicsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movichome import views
from django.conf.urls import url, include


from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from movichome.models import PageScrape, DBPScrape, MCPScrape


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ScrapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageScrape
        fields = ('title', 'text_id')

class MCPScrapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MCPScrape
        fields = ('title', 'MCPList', 'description_2', 'pub_date_mcp')

class DBPScrapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBPScrape
        fields = ('title', 'DBPDefinition', 'peribahasa', 'pantun', 'pub_date_dbp')

        

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ScrapViewSet(viewsets.ModelViewSet):
    queryset = PageScrape.objects.all()
    serializer_class = ScrapSerializer

class MCPScrapViewSet(viewsets.ModelViewSet):
    queryset = MCPScrape.objects.all()
    serializer_class = MCPScrapSerializer

class DBPScrapViewSet(viewsets.ModelViewSet):
    queryset = DBPScrape.objects.all()
    serializer_class = DBPScrapSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'scrap', ScrapViewSet)
router.register(r'dbp', DBPScrapViewSet)
router.register(r'mcp', MCPScrapViewSet)




urlpatterns = [
    #path("", hello.views.index, name="index"),
    path('', views.index), 
    path('about', views.about), 
    path('feedback', views.feedback), 
    path('search', include('movichome.url')),
    path('admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls'))

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



