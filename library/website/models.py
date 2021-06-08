from django.db import models

class LibraryCardModel(models.Model):
	user_email = models.CharField(max_length=40)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)

