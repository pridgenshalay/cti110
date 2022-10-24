#how to write code that displays information to users using if-else nested statements
# 24 Oct 2022
#CTI-110 P3 Lab- Leap Year
#Shalay Pridgen
#

is_leap_year = False

#input
#allows for user to input the year to determine whether or not it is a leap year
input_year = int(input('Enter year: '))

#process
#satifies the requirements, a leap year is determined by if it is divisible by 4 and in cases
#where centuries are involved, it is divisble by 400 
if (input_year % 4) == 0:
    if (input_year % 100) == 0:
        if (input_year % 400) == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

#output
#prints output with the year and its classification
if is_leap_year == True:
    print(f'{input_year} - is a leap year')
else:
    print(f'{input_year} - is NOT a leap year')


    

