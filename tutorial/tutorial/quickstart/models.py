from django.db import models

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length = 100, blank = False)
	content = models.TextField()
	author = models.CharField(max_length = 100, blank = False)

	class Meta:
		ordering = ['created']



class Book(models.Model):
	author_first_name = models.CharField(max_length = 100, blank = False)
	author_last_name = models.CharField(max_length = 100, blank = False)
	title = models.CharField(max_length = 100, blank = False)
	isbn = models.IntegerField()

	class Meta:
		ordering = ['isbn']