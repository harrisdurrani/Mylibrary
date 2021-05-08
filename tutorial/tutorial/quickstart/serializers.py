from rest_framework import serializers
from quickstart.models import Post, Book

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ['id', 'title', 'author', 'content']


class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['id', 'author_first_name', 'author_last_name', 'title', 'isbn']
