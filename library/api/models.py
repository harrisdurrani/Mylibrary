from django.db import models


class Book(models.Model):
	author_first_name = models.CharField(max_length = 100, blank = False)
	author_last_name = models.CharField(max_length = 100, blank = False)
	title = models.CharField(max_length = 100, blank = False)
	isbn = models.IntegerField()

	class Meta:
		ordering = ['isbn']