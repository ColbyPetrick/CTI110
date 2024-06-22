# Colby Petrick
# June 22nd 2024
# P2HW2
# Showcasing knowledge of lists

# Decided to keep my test portions within this file to see about recieving feedback on better methods/ways to do so
# I normally would delete them after assuring they work for the segment coded.

# Coded Segment 1
print('Enter grade for Module 1:', end = ' ')
module1 = float(input())

print('Enter grade for Module 2:', end = ' ')
module2 = float(input())

print('Enter grade for Module 3:', end = ' ')
module3 = float(input())

# print('Placeholder & Variabe check:', module1, module2, module3)

# Coded Segment 2
print('Enter grade for Module 4:', end = ' ')
module4 = float(input())

print('Enter grade for Module 5:', end = ' ')
module5 = float(input())

print('Enter grade for Module 6:', end = ' ')
module6 = float(input())

# print('Placeholder & Variable check:', module4, module5, module6)

# Coded Segment 3
gradebook = [module1, module2, module3, module4, module5, module6]
lowest = min(gradebook)
highest = max(gradebook)
avg = sum(gradebook) / len(gradebook)
total = sum(gradebook)
# print(f'Placeholder & Variable Check:, {lowest}, {highest}, {avg:.2f}, {total}')

# Coded Segment 4
print('\n------------Results------------')
print(f'Lowest Grade:       {lowest:.1f}')
print(f'Highest Grade:      {highest:.1f}')
print(f'Sum of Grades:      {total:.1f}')
print(f'Average:            {avg:.2f}')
print('----------------------------------------')

