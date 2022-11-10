from rest_framework.viewsets import ModelViewSet

from core.serializers import LivroSerializer, LivroDetailSerializer
from core.models import Livro


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroDetailSerializer
        return LivroSerializer
