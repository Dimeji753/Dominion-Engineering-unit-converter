# ENGINEERING UNIT CONVERTER
# ND1 Mechatronics Engineering
# CTE 123 Python Mini Project

# Store previous conversions
history = []


# Function to perform unit conversions
def convert_units(choice, value):

    if choice == 1:
        result = value / 25.4
        return result, "inches"

    elif choice == 2:
        result = value * 25.4
        return result, "mm"

    elif choice == 3:
        result = (value * 9/5) + 32
        return result, "Fahrenheit"

    elif choice == 4:
        result = (value - 32) * 5/9
        return result, "Celsius"

    elif choice == 5:
        result = value * 2.20462
        return result, "pounds"

    elif choice == 6:
        result = value / 2.20462
        return result, "kg"

    elif choice == 7:
        result = value / 3.6
        return result, "m/s"

    elif choice == 8:
        result = value * 3.6
        return result, "km/h"


# Main program
def main():

    while True:

        print("\n===== ENGINEERING UNIT CONVERTER =====")

        print("1. Millimetres to Inches")
        print("2. Inches to Millimetres")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Kilograms to Pounds")
        print("6. Pounds to Kilograms")
        print("7. km/h to m/s")
        print("8. m/s to km/h")
        print("9. View Conversion History")
        print("0. Exit")

        try:
            choice = int(input("\nChoose a conversion: "))

            if choice == 0:
                print("Thank you for using the converter!")
                break

            elif choice == 9:

                if len(history) == 0:
                    print("No conversion history available.")

                else:
                    print("\n===== CONVERSION HISTORY =====")

                    for item in history:
                        print(item)

            elif 1 <= choice <= 8:

                value = float(input("Enter the value to convert: "))

                result, unit = convert_units(choice, value)

                answer = f"{value} = {result:.2f} {unit}"

                print("\nConversion Result:")
                print(answer)

                # Save conversion in history
                history.append(answer)

            else:
                print("Invalid choice! Please select 0-9.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Run the program
main()