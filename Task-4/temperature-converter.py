# Function to display menu and get user choice
def display_menu():
    print("Temperature Converter")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit

# Main function to run the temperature converter
def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif choice == '3':
            print("Exiting Temperature Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Run the main function
if __name__ == "__main__":
    main()
