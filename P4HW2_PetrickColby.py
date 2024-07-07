# Colby Petrick
# July 7th 2024
# P4HW2
# Demonstrating knowledge of while loops

# Coded Segment One
x = 0 # Handles total employees
# Added the following 4 variables outside the loop to prevent unintended consequences regarding math + stops two errors from occuring
fullot = 0 
fullgross = 0
fullreg = 0
employname = 'placeholder' # To start the loop
while employname != 'Done':
    employname = input('Enter employee\'s name or "Done" to terminate: ')
    if employname == 'Done':
        break
    else:
        hourwrk = int(input('Enter number of hours worked: '))
        payrate = float(input('Enter employee\'s pay rate: '))
        x += 1


# Coded Segment Two
    if hourwrk <= 40:
        regpay = hourwrk * payrate
        overtime = 0
        overtimepay = 0
    else:
        overtimepay = (payrate * 1.5) * (hourwrk - 40) 
        overtime = hourwrk - 40
        hourwrk = 40
        regpay = hourwrk * payrate

    grosspay = overtimepay + regpay
    hourwrk = hourwrk + overtime 

# Coded Segment Three
    print('------------------------')
    print(f'Employee name: {employname}')

    print('\nHours Worked   Pay Rate   Overtime   OverTime Pay   RegHour Pay   Gross Pay')
    print('-----------------------------------------------------------------------------')
    print(f'{hourwrk:<14.1f} ${payrate:<9.1f} {overtime:<10.1f} ${overtimepay:<13.2f} ${regpay:<12.2f} ${grosspay:<5.2f}')

    fullot = overtimepay + overtimepay
    fullreg = regpay + regpay
    fullgross = grosspay + grosspay
# Coded Segment 4
print(f'\nTotal number of employees entered: {x}')
print(f'Total amount paid for overtime: ${fullot}')
print(f'Total amount paid for regular hours: ${fullreg}')
print(f'Total amount paid in gross: ${fullgross}')