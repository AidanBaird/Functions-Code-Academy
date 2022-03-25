current_budget = 3500.75
# Create a variable for shirt_expense
shirt_expense = 9
# Create a variable for new_budget_after_shirt
new_budget_after_shirt = 0
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))
  print("")

print_remaining_budget(current_budget)


# Create a new function that works out expenses by returning budget - expense
#help("return")
def deduct_expense(budget, expense):
  return budget - expense

# Run function to see current budget and make it = to new_budget_after_shirt
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

# Call function that prints our new found budget
print_remaining_budget(new_budget_after_shirt)
