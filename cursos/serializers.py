from rest_framework import serializers
from cursos.models import Avaliacao, Curso

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True} # configuração write_only só para escrever, isso quer dizer que não vai ser possível fazer consulta com GET
        }
        
        model = Avaliacao
        
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'publicacao',
            'ativo'
        )
        
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'publicacao',
            'ativo'
        )