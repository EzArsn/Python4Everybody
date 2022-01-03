# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

def main():
    print("Enter the temperature in celcius:\t", end='')
    c=input()
    c=float(c)
    f=1.8*c+32
    print(f"The temperature in farenheit is {f}F")
main()