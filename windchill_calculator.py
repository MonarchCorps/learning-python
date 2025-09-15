measurement = ""
temperature = input("What is the temperature? ")

def convert_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

def calculate_windchill(temp, speed):
    return 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + ((0.4275 * temp) * (speed ** 0.16))

if temperature.lstrip("-").isdigit():
    temperature = float(temperature)
    measurement = input("Fahrenheit or Celsius (F/C)? ").lower()

    while measurement not in ["f", "c"]:
        measurement = input("Please enter a valid measurement. (F/C): ").lower()

    if measurement == "c":
        temperature = convert_to_fahrenheit(temperature)

    for x in range(5, 61, 5):
        value = calculate_windchill(temperature, x)
        print(f"At temperature {temperature:.1f}F, and wind speed {x} mph, the windchill is: {value:.2f}F")

else:
    print("Invalid input")
