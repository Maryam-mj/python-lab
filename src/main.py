from utils import square, is_even, celsius_to_fahrenheit, greet

number = float(input("Enter a number: "))
name = input("Enter your name: ")

print("Square:", square(number))

if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")

print("Fahrenheit equivalent:", celsius_to_fahrenheit(number))

print(greet(name))