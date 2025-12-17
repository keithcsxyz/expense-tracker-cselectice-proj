from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Expense
from .forms import ExpenseForm
import csv
from django.urls import reverse


def index(request):
	qs = Expense.objects.all()
	month = request.GET.get('month')  # expected format: YYYY-MM
	if month:
		year, mon = month.split('-')
		qs = qs.filter(date__year=year, date__month=mon)

	context = {'expenses': qs, 'month': month}
	return render(request, 'expenses/index.html', context)


def add_expense(request):
	if request.method == 'POST':
		form = ExpenseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('expenses:index'))
	else:
		form = ExpenseForm()
	return render(request, 'expenses/form.html', {'form': form, 'title': 'Add Expense'})


def edit_expense(request, pk):
	obj = get_object_or_404(Expense, pk=pk)
	if request.method == 'POST':
		form = ExpenseForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			return redirect(reverse('expenses:index'))
	else:
		form = ExpenseForm(instance=obj)
	return render(request, 'expenses/form.html', {'form': form, 'title': 'Edit Expense'})


def delete_expense(request, pk):
	obj = get_object_or_404(Expense, pk=pk)
	if request.method == 'POST':
		obj.delete()
		return redirect(reverse('expenses:index'))
	return render(request, 'expenses/confirm_delete.html', {'object': obj})


def export_csv(request):
	qs = Expense.objects.all().order_by('date')
	month = request.GET.get('month')
	if month:
		year, mon = month.split('-')
		qs = qs.filter(date__year=year, date__month=mon)

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="expenses.csv"'

	writer = csv.writer(response)
	writer.writerow(['date', 'description', 'category', 'amount', 'notes'])
	for e in qs:
		writer.writerow([e.date, e.description, e.category, str(e.amount), e.notes])

	return response
