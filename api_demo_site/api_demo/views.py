from rest_framework import viewsets
from api_demo_site.api_demo.models import Stuff
from api_demo_site.api_demo.serializers import StuffSerializer


class StuffViewSet(viewsets.ModelViewSet):
    """ An endpoint in the API that allows Stuff to be viewed and edited.
    """

    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
