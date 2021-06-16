from django.db import models
from django.contrib.auth.models import User as user_model


class LibraryCardModel(models.Model):
	user_email = models.CharField(max_length=40)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	library_card_id = models.AutoField(primary_key=True)
	owner = models.OneToOneField(user_model, on_delete=models.CASCADE, null=True, default=None)

	def __str__(self):
		return str(self.library_card_id)