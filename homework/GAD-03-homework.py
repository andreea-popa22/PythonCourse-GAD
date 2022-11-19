# Write a function that takes an undefined number of parameters and calculate
# the sum of the parameters that represent integers or real numbers
def function1(*args, **kwargs):
    sum = 0.0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            sum += arg
    return sum


print("--1--")
print(function1(1, 5, -3, 'abc', [12, 56, 'cad']))
print(function1())
print(function1(2, 4, 'abc', param_1=2))


# Write a recursive function that takes an integer as a parameter and returns:
# sum of all numbers from [0, n]
def function2(n):
    if n == 0:
        return 0
    return n + function2(n-1)

print("--2--")
print(function2(4))


# Write a recursive function that takes an integer as a parameter and returns:
# sum of even numbers from [0, n]
def function3(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + function3(n-1)
    return function3(n-1)

print("--3--")
print(function3(5))
print(function3(6))


# Write a recursive function that takes an integer as a parameter and returns:
# sum of odd numbers from [0. n]
def function4(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n + function4(n-1)
    return function4(n-1)

print("--4--")
print(function4(4))
print(function4(5))


# Write a function that reads from the keyboard and returns
# the value if it is an integer, otherwise it returns the value 0.
def function5():
    x = input("Your value: ")
    if x.isdigit():
        return x
    return 0

print("--5--")
print(function5())
