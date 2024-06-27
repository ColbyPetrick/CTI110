# Colby Petrick
# June 27th 2024
# P3 Lab
# Demonstrating knowledge of various else-if statements & Arithmatic functions

# Coded Segment One
money = float(input('Enter the amount of money as a float: $'))

totchange = int(money * 100)
dollar = totchange // 100
remainder = totchange % 100
quarters = remainder // 25
remainder = remainder % 25
dimes = remainder // 10
remainder = remainder % 10
nickels = remainder // 5
pennies = remainder % 5
# Segment One Testing proved accurate - Using modulo seemed more effective then subtraction
# print('totchange:', totchange, 'dollar:', dollar, 'quarters:', quarters, 'dimes:', dimes, 'nickels:', nickels, 'pennies:', pennies)

# Coded Segment Two

# I feel this could have been shortened however this gets the achieved affect - I was also unsure
# About how to shorten this without making it nested and wasn't 100% sure that would work w/o issue no matter input
if (dollar <= 0) and (quarters <= 0) and (dimes <= 0) and (nickels <= 0) and (pennies <= 0):
    print('No Change')
# Using multiple if statements at once to ensure one 0 return won't cause issues

if (dollar > 0):
    print(dollar, 'Dollars')

if (quarters == 1):
    print(quarters, 'Quarter')
elif (quarters > 1):
    print(quarters, 'Quarters')

if (dimes == 1):
    print(dimes, 'Dime')
elif (dimes > 1):
    print(dimes, 'Dimes')

if (nickels == 1):
    print(nickels, 'Nickel')
elif (nickels > 1):
    print(nickels, 'Nickels')

if (pennies == 1):
    print(pennies, 'Penny')
elif (pennies > 1):
    print(pennies, 'Pennies')

# Code output is as expected - and accurate based off how we would give change back
# whilst on a register

# Had to move from Github codespace to IDLE as it was having issues syncing
