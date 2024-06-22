# Colby Petrick
# June 22nd 2024
# P2LAB2
# Demonstrating understanding of using dictionarys

# Coded Segment 1
cars = {
    'Camaro':18.21,
    'Prius':52.36,
    'Model S':110,
    'Silverado':26
}

keys = cars.keys()
print(keys)

# Coded Segment 2
print('\nEnter a vehicle to see it\'s mpg:', end = ' ')
carselect = input()

print('\nThe', carselect, 'gets', cars[carselect], 'mpg.')
# Spent a bit of time over-thinking this segment but got it working

# Coded Segment 3
print('\nHow many miles will you drive the', carselect + '?', end = ' ')
drivemiles = int(input())

mpgusage = drivemiles / cars[carselect]

print(f'\n{mpgusage:.2f} gallon(s) of gas are needed to drive the {carselect} {drivemiles:.1f} miles.')
