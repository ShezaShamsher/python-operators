# Operators

# 1.Arithematic operator
a : int = 5 
b : int = 2

print("Arithematic Operators")
print("a + b = ", a + b)     # Addition
print("a - b = ", a - b)     # Subtraction
print("a * b = ", a * b)     # Multiplication
print("a / b = ", a / b)     # Division
print("a // b = ", a // b)   # Floor Division
print("a ** b = ", a ** b )  # Exponentiation
print("a % b = ", a % b)     # Modulus
 
# 2.Comparsion Operators
c : int = 15
d : int = 10

print("Comparsion Operators")
print("c == d = ", c == d)     # Equal
print("c != d = ", c != d)     # not equal
print("c > d = ", c > d)       # Greater than
print("c < d = ", c < d)       # Less than
print("c >= d = ", c >= d)     # Greater than or equal 
print("c <= d = ", c <= d)     # Less than or equal

# 3.Logical Operators
y : bool = True
z : bool = False

print("Logical Operators")
print("y and z = ", y and z ) 
print("y or z = ", y or z )
print("not y  = ", not y )

# 4. Assignment Operators 
x = 7

print("Assignment Operators")

print("x = ", x)         # Assignment 
x += 3
print("x += 3 = ", x)    # Addition Assignment
x -= 3
print("x -= 3 = " , x)   # Subtraction Assignment
x *= 7
print("x *= 7 = ", x)    # Multiplication Assignment
x /= 4
print("x /= 4 = ", x)    # Division Assignment
x //= 4 
print("x //= 4 = ", x)   # Floor Division Assignment

# 5.Identity Operators

m : list = [1, 2, 3]
n : list = [1, 2, 3]
o : list = m

print("Identity Operators")

print("m is o = ", m is o)
print("m is n = ", m is n)
print("m == n = ", m == n )
print("m is not n = ", m is not n)

print("\n ----- \n")

print(id(m))
print(id(n))
print(id(o))

# 6.Membership Operators

fruit : str = 'Apple'

print("Membership Operators")

print("Apple in fruit = ", 'Apple' in fruit)
print("Mango not in fruit = ", 'Mango' not in fruit)

# 7.Bitwise Operators
r : int = 5
s : int = ~r
 
print("Bitwise Operators")

print("y = ", y)

# bin() function

print("bin(r) = ", bin(r), type(bin(r)) )