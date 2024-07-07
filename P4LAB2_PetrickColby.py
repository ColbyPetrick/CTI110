# Colby Petrick
# July 7th 2024
# P4LAB2
# Utilization of While & For Loops to demonstrate understanding

# Coded Segment One
runagain = 'yes' # On first attempt made an infinite loop due to indentation
while runagain == 'yes':
    usin = int(input('Enter a number: '))
    print()
    if usin >= 0:
        for x in range(1, 13):
            result = usin * x
            x += 1
            print(f'{usin} * {x - 1} = {result}')
        print()
        runagain = input('Would you like to run the program again? ')
    else:
        print('This program does not handle negative numbers.')
        runagain = input('Would you like to run the program again? ')

if runagain == 'no':
    print()
    print('Exiting program...')

# The following was mostly done just by using the already existing
# Print functions to get a better idea of how it was looking
# Including spacing & accuracy