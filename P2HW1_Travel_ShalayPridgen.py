#Changing how the results of the previous travel project are displayed
#5 Oct 2022
#CTI-110 P2HW1- Travel
#Shalay Pridgen
#

#Input
#The program allows the user to enter numbers for each statement

print('This program calculates and displays travel expenses.')
print()
budget = float(input('Enter Budget: '))
print()
dest = input('Enter your travel destination:',)
print()
gasoline = float(input('How much do you think you will spend on gas: '))
print()
accomdation = float(input('How much do you think you will spend on accomdation: '))
print()
food = float(input('How much do you need for food: '))
print()


# The program displays the user entered numbers for each statement
#The program will also align each statement
print('------Travel Expenses--------')
print("{:25}{:<5}".format("Location:", dest))
print("{:25}{:>1}{:<5}".format("Initial Budget:","$", budget))
print("{:25}{:>1}{:<5}".format("Fuel:","$", gasoline))
print("{:25}{:>1}{:<5}".format("Accomodation:", "$",accomdation))
print("{:25}{:>1}{:<5}".format("Food:","$",food))
print('-------------------------------')
#process
#The program takes the numbers from each statement
#and adds the gas, accomdation, and food together to subtract that from the budget.

expense = int(food + accomdation + gasoline)
remBud = budget - expense

#output
#The program displays the final number Remaining Balance given by the last statement 
print()
print("{:25}{:>1}{:<5}".format("Remaining Balance:", "$",remBud))
