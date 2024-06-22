# Colby Petrick
# June 22nd 2024
# P2HW1
# Updating P1HW1

#Visual spacing between statements for readability
print('This program calculates and displays travel expenses\n')

print('Enter Budget:', end=' ')
budget = int(input())

print('\nEnter your travel destination:', end=' ')
dest = input()

print('\nHow much do you think you will spend on gas?', end=' ')
gas = int(input())

print('\nApproximately, how much will you need for accomodation/hotel?', end=' ')
shelter = int(input())

print('\nLast, how much do you need for food?', end=' ')
food = int(input())

# Expenses Portion
print('\n------------Travel Expenses------------')
print(f'Location:           ${dest}')
print(f'Initial Budget:     ${budget:.2f}')
print(f'Fuel:               ${gas:.2f}')
print(f'Accomodation:       ${shelter:.2f}')
print(f'Food:               ${food:.2f}')
print('---------------------------------------')

# Remainder
remainder = budget - gas - shelter - food
print(f'\nRemaining Balance: ${remainder:.2f}')

'''
Adding a "Planned Days" input and multiplying
Accomodation, Food and potentially Fuel by planneddays
could give a more accurate definition unless your doing a one day permanent trip
'''