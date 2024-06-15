# Colby Petrick
# June 15th 2024
# P1HW2
# Demonstrating knowledge of input/output w/ variable and print basics

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

#grouping here for self visualization
print('\n\n------------Travel Expenses------------')
print('Location:', dest)
print('Initial Budget:', budget)

print('\nFuel:', gas)
print('Accomodation:', shelter)
print('Food:', food)

remainder = budget - gas - shelter - food
print('\nRemaining Balance:', remainder)