# Write a Python program that computes the greatest common divisor
# (GCD) of two positive integers

def lcm(x, y):
    if x > y:
        z = x

    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm
print(lcm(4, 6))
print(lcm(15, 17))


##################################################################


# Write a Python program to sum two given integers. However,
# if the sum is between 15 and 20 it will return 20.


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):

        return 20
    else:
        return sum



print(sum(1, 2))
print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))

#######################################################

# Write a Python program that returns true if the two given
# integer values are equal or their sum or difference is 5.


def test_number5(x,y):
    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    else:
        return False

print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))


################################################################3

# Write a Python program to calculate the distance between the
# points (x1, y1) and (x2, y2).
import math

x2 = 4
x1 = 0
y1 = 6
y2 = 6

# def dist(x1, x2, y1, y2):
distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))



print(distance)


##################################################

# Write a Python program to convert height (in feet and inches)
# to centimeters.

print("Input your height: ")
h_ft = int(input("feet: "))
h_inch = int(input("inches: "))

calch = h_ft * 30.48
calcI = h_inch * 2.54

h_cm = calch + calcI

print(h_cm)


######################################################


