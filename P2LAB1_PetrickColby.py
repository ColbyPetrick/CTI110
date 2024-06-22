# Colby Petrick
# June 22nd 2024
# P2LAB1
# Showcasing knowledge of mathematical calculation & display within python
import math
# Imported math module to simplify pi.

print('What is the radius of the circle?', end = ' ')
radiusin = float(input())

# The following segment was tested using three combinations of numbers

diameter = 2 * radiusin
circumference = 2 * math.pi * 4
area = math.pi * radiusin**2
print(f'The diameter of the circle is {diameter:.2f}')
print(f'The circumference of the circle is {circumference:.2f}')
print(f'The area of the circle is {area:.3f}')
