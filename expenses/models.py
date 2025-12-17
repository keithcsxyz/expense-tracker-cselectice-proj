from django.db import models


class Expense(models.Model):
	CATEGORY_CHOICES = [
		('food', 'Food'),
		('transport', 'Transport'),
		('rent', 'Rent'),
		('utilities', 'Utilities'),
		('entertainment', 'Entertainment'),
		('other', 'Other'),
	]

	description = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()
	category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
	notes = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date', '-created_at']

	def __str__(self):
		return f"{self.date} — {self.description} ({self.amount})"
