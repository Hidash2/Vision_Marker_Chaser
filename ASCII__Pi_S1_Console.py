from time import sleep
from math import sin, cos, radians

# Demo - prints a sine curve with * and cos curve with #
# Modified to print something readable on the S1 Console
for n in range(28, 90):
    circle_1 = 25 * (1 + sin(radians(n * 10)))
    # circle_2 = 50 * (1 + cos(radians(n * 10)))
    # print("#".center(int(circle_1)))
    print()
    for i in range(int(circle_1)):
        print('*', end='')
    # print("#".center(int(circle_2)))
    # print(circle_2)
    sleep(0.25)
