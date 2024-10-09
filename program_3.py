# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
def calculate_sales_tax(total_sales):
  state_tax_rate = 0.05
  county_tax_rate = 0.025

  county_sales_tax = total_sales * county_tax_rate
  state_sales_tax = total_sales * state_tax_rate
  total_sales_tax = county_sales_tax + state_sales_tax


  return county_sales_tax, state_sales_tax, total_sales_tax

# Get total sales
total_sales = float(input("Enter the total sales for the month: $"))

# Calculate sales taxes
county_sales_tax, state_sales_tax, total_sales_tax = calculate_sales_tax(total_sales)


# Print the results
print("County Sales Tax: $", county_sales_tax)
print("State Sales Tax: $", state_sales_tax)
print("Total Sales Tax: $", total_sales_tax)

#Jadon Anderstrom, 10/08/24, "Tax Rate".
