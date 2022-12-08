# CTI-110
# P4HW2 - Salary Calculator
# Shalay Pridgen 
# 16 Nov 2022
#

#input and process are sort of intermingled 
#set variables for the totals
total_employees = 0              
total_OverTimePay = 0       
total_RegPay = 0            
total_GrossPay = 0          


while True:
    name = input("Enter employee's name or \"None\" to terminate: ")
    if name == "None":
        break
    else:
        total_employees += 1
    
    hours_worked = float(input("How many hours did " + name + " work? "))
    pay_rate = float(input("What is " + name + "\' pay rate? "))
    
    #set variables 
    overTime = 0
    overtime_Pay = 0
    reg_Pay = 0
    gross_Pay = 0
    
    if hours_worked > 40:
        overTime = hours_worked - 40
        overtime_Pay = overTime * pay_rate * 1.5
        reg_Pay = 40*pay_rate
        gross_Pay = reg_Pay + overtime_Pay
    else:
        
        # calculate regular Pay and gross pay
        reg_Pay = hours_worked *pay_rate
        gross_Pay = reg_Pay
        
    total_OverTimePay += overtime_Pay
    total_RegPay += reg_Pay
    total_GrossPay += gross_Pay

    #output
    print("\nEmployee name: " + name + "\n")
    
    # and then print all the abover calculate values in tabular format as per the given format
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-------------------------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours_worked, pay_rate, overTime, overtime_Pay, reg_Pay, gross_Pay))
    print()

# once the loop terminates, print number of employees entered, total over time pay, total regular pay, and total gross pay
print()
print("Total number of employees entered:", total_employees)
print("Total amount payed for over time: $" + '{:.2f}'.format(total_OverTimePay))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(total_RegPay))
print("Total amount payed in gross: $" + '{:.2f}'.format(total_GrossPay))
