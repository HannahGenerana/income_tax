# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000      	0
# Next $10,000	       10
# The remaining	       20

# pseudocode

# create a function to consider each rule
def calculate_income_tax (income):

# print the given income
  tax_payable = 0
  print (f"The given income is ${income}")

# check the conditions
  # income is less than 10000
  if income <= 10000:
    tax_payable = 0

  # income is less than 20000
  elif income <= 20000:
    next_taxable_income = income - 10000
    tax_payable = next_taxable_income * 10 / 100

   # applying the rules to the income
  else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

# print the result

# print the result of the example