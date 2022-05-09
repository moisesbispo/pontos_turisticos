from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class AtracaoSerializers(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('nome', 'descricao', 'horario_func', 'idade_minima')