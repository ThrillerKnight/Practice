# Temperature Converter
# This project allows you to convert temperatures between Celsius, Fahrenheit, and Kelvin. 

# Convert Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

# Convert Celsius to Kelvin
def c_to_k(celsius):
    return celsius + 273.15

# Convert Fahrenheit to Celsius
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Convert Fahrenheit to kelvin
def f_to_k(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Convert Kelvin to Celsius
def k_to_c(kelvin):
    return kelvin - 273.15

# Convert Kelvin to Fahrenheit
def k_to_f(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# User input for the temperature value and the conversion type
temp = float(input("Enter the temperature you want to convert: "))
print("Choose the conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")
choice = int(input("Enter your choice (1-6): "))

# Perform the conversion
if choice == 1:
    print(f"{temp} Celsius is {c_to_f(temp)} Fahrenheit.")
elif choice == 2:
    print(f"{temp} Celsius is {c_to_k(temp)} Kelvin.")
elif choice == 3:
    print(f"{temp} Fahrenheit is {f_to_c(temp)} Celsius.")
elif choice == 4:
    print(f"{temp} Fahrenheit is {f_to_k(temp)} Kelvin.")
elif choice == 5:
    print(f"{temp} Kelvin is {k_to_c(temp)} Celsius.")
elif choice == 6:
    print(f"{temp} Kelvin is {k_to_f(temp)} Fahrenheit.")
else:
    print("Invalid choice. Please select a number between 1 and 6.")