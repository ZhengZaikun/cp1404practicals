"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
def main():
    """Convert temperature units by inputting temperature"""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            temperature = celsius
            fahrenheit = convert_units(choice, temperature)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            temperature = fahrenheit
            celsius = convert_units(choice, temperature)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_units(choice, temperature):
    """Converts temperature units and returns the value of another temperature"""
    if choice == "C":
        fahrenheit = temperature * 9.0 / 5 + 32
        return fahrenheit
    elif choice == "F":
        celsius = 5 / 9 * (temperature - 32)
        return celsius

main()