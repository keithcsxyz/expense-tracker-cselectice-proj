from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	list_display = ('date', 'description', 'category', 'amount')
	list_filter = ('category', 'date')
	search_fields = ('description', 'notes')
	ordering = ('-date',)
