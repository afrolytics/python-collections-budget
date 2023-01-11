from budget import Expense
import collections

# call Expense.Expenses constructor
expenses = Expense.Expenses

expenses.read_expenses(expenses, filename='data/spending_data.csv')

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)
