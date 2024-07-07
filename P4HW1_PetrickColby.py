# Colby Petrick
# July 7th 2024
# P4HW1
# Demonstrating knowledge of loops with lists & Nested Loops

# Coded Segment One
for x in range(1, 7):
    print('Enter grade for Module 1:', end = ' ')
    module1 = float(input())
    while module1 < 0 or module1 > 100:
        print('\nError: Invalid Score!')
        print('Scores should be between 0 and 100')
        module1 = float(input('Enter Module 1 grade: '))
    

    print('Enter grade for Module 2:', end = ' ')
    module2 = float(input())
    while module2 < 0 or module2 > 100:
        print('\nError: Invalid Score!')
        print('Scores should be between 0 and 100')
        module2 = float(input('Enter Module 2 grade: '))

    print('Enter grade for Module 3:', end = ' ')
    module3 = float(input())
    while module3 < 0 or module3 > 100:
        print('\nError: Invalid Score!')
        print('Scores should be between 0 and 100')
        module3 = float(input('Enter Module 3 grade: '))

# Coded Segment Two
    print('Enter grade for Module 4:', end = ' ')
    module4 = float(input())
    while module4 < 0 or module4 > 100:
        print('\nError: Invalid Score!')
        print('Scores should be between 0 and 100')
        module4 = float(input('Enter Module 4 grade: '))

    print('Enter grade for Module 5:', end = ' ')
    module5 = float(input())
    while module5 < 0 or module5 > 100:
        print('\nError: Invalid Score!')
        print('Scores should be between 0 and 100')
        module5 = float(input('Enter Module 5 grade: '))

    print('Enter grade for Module 6:', end = ' ')
    module6 = float(input())
    while module6 < 0 or module6 > 100:
        print('\nError: Invalid Score!')
        print('Scores should be between 0 and 100')
        module6 = float(input('Enter Module 6 grade: '))
    break

# Coded Segment Three
gradebook = [module1, module2, module3, module4, module5, module6]
lowest = min(gradebook)
avg = sum(gradebook) / len(gradebook)
modif = gradebook.remove(min(gradebook))

if avg >= 90 and avg <= 100:
    letgrad = 'A'
elif avg >= 80 and avg <= 89:
    letgrad = 'B'
elif avg >= 70 and avg <= 79:
    letgrad = 'C'
elif avg >= 60 and avg <= 69:
    letgrad = 'D'
else:
    letgrad = 'F'
print('\n------------Results------------')
print(f'Lowest Score  :  {lowest:.1f}')
print(f'Modified List :  {gradebook}')
print(f'Scores Average:  {avg:.2f}')
print(f'Grade         :  {letgrad}')
print('----------------------------------------')

# Notes: As I still haven't gotten a great understanding on loops I opted to use an else-if for the Letter Grade

