from rest_framework import serializers
from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'rating', 'genre', 'genre_name', 'owner', 'created_at']