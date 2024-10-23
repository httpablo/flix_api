from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializers


class ActorCreateListView(generics.ListCreateAPIView):
	queryset = Actor.objects.all()
	serializer_class = ActorSerializers


class ActorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Actor.objects.all()
	serializer_class = ActorSerializers
