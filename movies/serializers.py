from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    #genre = serializers.StringRelatedField()  # Retorna o nome do gênero em vez do ID
    #actors = serializers.StringRelatedField(many=True)  # Retorna os nomes dos atores em vez dos IDs

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        return 5
    
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não pode ser maior que 200 caracteres.')
        return value