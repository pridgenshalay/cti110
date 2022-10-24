# 24 Oct 2022
#CTI-110 P3 HW1 - Debugging
#Shalay Pridgen
# 


# This program takes a number grade, determines average and displays letter grade for average.

#input
#Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print()

#process
#add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
avg = sum(grades) / len(grades)

print('-----------Results----------')
print("{:25}{:<5}".format("Lowest Grade:", min(grades)))
print("{:25}{:<5}".format("Highest Grade:", max(grades)))
print("{:25}{:<5}".format("Sum of Grades:", sum(grades)))
print("{:25}{:<5}".format("Average:", f'{avg:.2f}'))
print('------------------------------------------')
# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
    
elif avg >= 80:
    print('Your grade is: B')

elif avg >= 70:
    print('Your grade is : C')

elif avg >= 60:
    print('Your grade is: D')
    
else:
    print('Your grade is: F')





