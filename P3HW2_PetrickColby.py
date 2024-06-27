# Colby Petrick
# June 27th 2024
# P3HW2
# Demonstrating knowledge regarding formatting & functions

# Coded Segment One
employname = input('Enter employee\'s name: ')
hourwrk = int(input('Enter number of hours worked: '))
payrate = float(input('Enter employee\'s pay rate: '))

# print(employname, hourwrk, payrate) - Used to test inputs and ensure they functioned

# Coded Segment Two
# Most of the math is in this segment
overtimepay = (payrate * 1.5) * (hourwrk - 40)

# If Statement here ensures the Reg Pay will always be calculating a flat 40 or lower - to ensure it is not calculating the OT
if hourwrk <= 40:
    regpay = hourwrk * payrate
    overtime = 0
else:
    overtime = hourwrk - 40
    hourwrk = 40
    regpay = hourwrk * payrate

grosspay = overtimepay + regpay
hourwrk = hourwrk + overtime # Had to conver hourwrk back to original input - I almost didn't catch this mistake
# print(overtimepay, regpay, grosspay, overtime) Used with the numbers in image & several others to ensure accuracy

# Coded Segment Three
print('------------------------')
print(f'Employee name: {employname}')

print('\nHours Worked   Pay Rate   Overtime   OverTime Pay   RegHour Pay   Gross Pay')
print('-----------------------------------------------------------------------------')
print(f'{hourwrk:<14.1f} ${payrate:<9.1f} {overtime:<10.1f} ${overtimepay:<13.2f} ${regpay:<12.2f} ${grosspay:<5.2f}')
