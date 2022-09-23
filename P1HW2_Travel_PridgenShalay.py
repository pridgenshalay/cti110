# A brief description of the project
# 21 September 2022
# CTI-110 P1HW2 - Travel Expense
# Shalay Pridgen

#Input
#The program allows the user to enter numbers for each statement

print('This program calculates and displays travel expenses.')
print()
budget = int(input('Enter Budget: '))
print()
dest = input('Enter your travel destination:' )
print()
gas = int(input('How much do you think you will spend on gas: '))
print()
accomdation = int(input('How much do you think you will spend on accomdation: '))
print()
food = int(input('How much do you need for food: '))
print()

# The program displays the user entered numbers for each statement

print('---travel expenses---')
print()
print('Location:' , dest)
print('Initial Budget: ', budget)
print()
print('Fuel: ', gas)
print('Accomdation: ', accomdation)
print('Food: ', food)
print()
#process
#The program takes the numbers from each statement
#and adds the gas, accomdation, and food together to subtract that from the budget.

expense = int(food + accomdation + gas)
remBud = budget - expense

#output
#The program displays the final number Remaining Balance given by the last statement 

print('Remaining Balance: ', remBud)
