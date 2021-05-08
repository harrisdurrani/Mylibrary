from rest_framework import serializers
from api.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['id', 'author_first_name', 'author_last_name', 'title', 'isbn']
