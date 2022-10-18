from rest_framework.serializers import ModelSerializer

from core.models import Editora, Livro


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
