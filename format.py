x = 30
print("x=/%16d/" % x)
print("x=/%-16d/" % x)
y = 65
print(format(y, "#b"))
print(format(y, "#o"))
print(format(y, "#x"))
z = 123.456
print("z=/%06.5f/" % z)
print("z=/{:06.5f}/".format(z))


# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))
print("The float number is:{:f}".format(12345555556.4566667898))
print("The float number is:{:10.6f}".format(12345555556.4566667898))
import decimal
g = decimal.Decimal('12345555556.4566667898')
print("The float number is:{:10.10f}".format(12345555556.4566667898))
print("The float number is:{:10.10f}".format(g))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))


print('------Number formatting with padding for int and floats')
# integer numbers with right alignment
print("{:5d}".format(12))
# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

print("{:^1.3f}".format(12.2345))

print("{:^10.20f}".format(12.2345))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))



print("------Number formatting for signed numbers")
# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))




print("------Number formatting with alignment")
# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))

# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters
# and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letters,
# padding and center alignment
print("{:^5.3}".format("caterpillar"))
print("{:>5.3}".format("caterpillar"))
print("{:*^5.3}".format("caterpillar"))

# define Person class
class Person:
    age = 23
    name = "Adam"

# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{name}'s age is: {age}".format(**person))


# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))
# Error
# print(num.format(123.236, aligns='<', width=8, precision=2))

import datetime
# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))
complexNumber2 = complexNumber + 3 + 5j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber2))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'
print("Adam's age is: {:age}".format(Person()))

# __str__() and __repr__() shorthand !r and !s
print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))

# __str__() and __repr__() implementation for class
class Person:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

print("repr: {p!r}, str: {p!s}".format(p=Person()))

class Cat(Person):
    def __str__(self):
        return "Str"
print("{c!s} and {c!r}".format(c=Cat()))
c=Cat()
print(f"{c} and {c}")
