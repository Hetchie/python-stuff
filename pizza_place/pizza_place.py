# pizza place

How_Many_pizzas = eval(raw_input("How many pizzas do you want?\n"))
Cost_Per_Pizza = 12.25
subtotal = How_Many_pizzas * Cost_Per_Pizza
Tax = 00.10
Sales_Tax = subtotal * Tax
total = subtotal + Sales_Tax
print"the total cost is $", total
print"this includes $", subtotal, "for the pizza and"
print"$", Sales_Tax, "in sales tax."