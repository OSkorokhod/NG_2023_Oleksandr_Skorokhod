


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("Choose an option:")
print("1. Convert from Celsius to Fahrenheit")
print("2. Convert from Fahrenheit to Celsius")

choice = int(input("Enter the option number (1/2): "))

if choice == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"Temperature in Celsius: {celsius}°C")
else:
    print("Invalid choice. Please choose 1 or 2.")