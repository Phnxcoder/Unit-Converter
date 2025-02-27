def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def meters_to_miles(meters):
    return meters / 1609.34

def miles_to_meters(miles):
    return miles * 1609.34

def feet_to_inches(feet):
    return feet * 12

def inches_to_feet(inches):
    return inches / 12

def kilograms_to_grams(kg):
    return kg * 1000

def grams_to_kilograms(g):
    return g / 1000

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

def pounds_to_ounces(lb):
    return lb * 16

def ounces_to_pounds(oz):
    return oz / 16


def unit_converter():
    while True:
        print("\n📏 Unit Converter 📏")
        print("1. Temperature (Celsius, Fahrenheit, Kelvin)")
        print("2. Length (Meters, Kilometers, Miles, Feet, Inches)")
        print("3. Weight (Kilograms, Grams, Pounds, Ounces)")
        print("4. Exit")

        choice = input("Select a category (1-4): ").strip()

        if choice == "1":  # Temperature Conversion
            print("\n🌡️ Temperature Conversions 🌡️")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            sub_choice = input("Choose conversion (1-4): ").strip()

            temp = float(input("Enter temperature: "))

            if sub_choice == "1":
                print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
            elif sub_choice == "2":
                print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
            elif sub_choice == "3":
                print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
            elif sub_choice == "4":
                print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
            else:
                print("Invalid choice!")

        elif choice == "2":  # Length Conversion
            print("\n📏 Length Conversions 📏")
            print("1. Meters to Kilometers")
            print("2. Kilometers to Meters")
            print("3. Meters to Miles")
            print("4. Miles to Meters")
            print("5. Feet to Inches")
            print("6. Inches to Feet")
            sub_choice = input("Choose conversion (1-6): ").strip()

            length = float(input("Enter length: "))

            if sub_choice == "1":
                print(f"{length} meters = {meters_to_kilometers(length):.2f} kilometers")
            elif sub_choice == "2":
                print(f"{length} kilometers = {kilometers_to_meters(length):.2f} meters")
            elif sub_choice == "3":
                print(f"{length} meters = {meters_to_miles(length):.2f} miles")
            elif sub_choice == "4":
                print(f"{length} miles = {miles_to_meters(length):.2f} meters")
            elif sub_choice == "5":
                print(f"{length} feet = {feet_to_inches(length):.2f} inches")
            elif sub_choice == "6":
                print(f"{length} inches = {inches_to_feet(length):.2f} feet")
            else:
                print("Invalid choice!")

        elif choice == "3":  # Weight Conversion
            print("\n⚖️ Weight Conversions ⚖️")
            print("1. Kilograms to Grams")
            print("2. Grams to Kilograms")
            print("3. Kilograms to Pounds")
            print("4. Pounds to Kilograms")
            print("5. Pounds to Ounces")
            print("6. Ounces to Pounds")
            sub_choice = input("Choose conversion (1-6): ").strip()

            weight = float(input("Enter weight: "))

            if sub_choice == "1":
                print(f"{weight} kg = {kilograms_to_grams(weight):.2f} grams")
            elif sub_choice == "2":
                print(f"{weight} grams = {grams_to_kilograms(weight):.2f} kg")
            elif sub_choice == "3":
                print(f"{weight} kg = {kilograms_to_pounds(weight):.2f} pounds")
            elif sub_choice == "4":
                print(f"{weight} pounds = {pounds_to_kilograms(weight):.2f} kg")
            elif sub_choice == "5":
                print(f"{weight} pounds = {pounds_to_ounces(weight):.2f} ounces")
            elif sub_choice == "6":
                print(f"{weight} ounces = {ounces_to_pounds(weight):.2f} pounds")
            else:
                print("Invalid choice!")

        elif choice == "4":  # Exit
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option, please try again!")


# Run the unit converter
unit_converter()
