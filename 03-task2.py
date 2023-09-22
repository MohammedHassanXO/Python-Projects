'''
Make a temperature/measurement converter. Write a script that can convert Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different ways
'''

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def inches_to_centimeters(inches):
    """Converts inches to centimeters"""
    centimeters = inches * 2.54
    return centimeters

def centimeters_to_inches(centimeters):
    """Converts centimeters to inches"""
    inches = centimeters / 2.54
    return inches

cond = "continue"
while cond == "continue" :
    print("Select the operation you want : to celsius, to fahrenheit, to centimmeters, to inches. ")
    operation = input("==>", )
    operation_value = float(input("Enter the value : ", ))

    if operation == 'celsius' :
        print(fahrenheit_to_celsius(operation_value))
    elif operation == 'fahrenheit' :
        print(celsius_to_fahrenheit(operation_value))
    elif operation == 'centimeters' :
        print(inches_to_centimeters(operation_value))
    elif operation == 'inches' :
        print(centimeters_to_inches(operation_value))
    
    cond = input("Continue or Break ?", )
    if cond == "break" :
        break
