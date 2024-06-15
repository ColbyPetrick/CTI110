# Colby Petrick
# June 15th 2024
# P1HW1
# Utilizing integer based inputs to demonstrate basic understanding

print('-----Calculating Exponents----')
print('\n\nEnter an integer as the base value:', end=' ')
num1 = int(input())
print('Enter an integer as the exponent:', end=' ')
num2 = int(input())
#Using two \n's for spacing as needed where possible
# This was tested using google to verify accuracy for: 15^3, 30^30 and 5^5 with accurate result
expo = num1 ** num2

print() #Used two prints here for spacing as attempting it with \n caused it to be pushed out
print()
print(num1, 'raised to the power of', num2, 'is', expo, '!!')
#adding space to make it easier to decipher segments

print('\n\n-----Addition and Subtraction----\n\n')
print('Enter a Starting integer:', end=' ')
num3 = int(input())
print('Enter an integer to add:', end=' ')
num4 = int(input())
print('Enter an integer to subtract:', end=' ')
num5 = int(input())

#Above inputs where tested using a temporary placeholder print after
#Issues given where fixed after double checking
total = num3 + num4 - num5
#Used print twice again for spacing purposes
print()
print()
print(num3, '+', num4, '-', num5, 'is equal to', total)