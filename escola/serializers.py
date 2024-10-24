from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate_cpf(self, cpf):
        if len( cpf ) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos!')        
        return cpf
    def validate_nome(self,nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O NOME só pode ter letras')
        return nome
    def validate_celular(self,celular):
        if len( celular ) != 13:
            raise serializers.ValidationError('O CELULAR precisa ter 13 dígitos!')        
        return celular


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerialializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields=['estudante_nome']