"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

user_sales = int(input("user's sales: "))
while user_sales >= 0:
    if user_sales < 1000:
        bonus = user_sales * .1
    else:
        bonus = user_sales * .15
    print("The user's bonus is $", bonus, sep="")
    user_sales = int(input("user's sales: "))
