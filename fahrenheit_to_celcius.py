#!/usr/bin/python3

def fahr_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

fahr = int(input('Enter temperature in Fahrenheit please: '))

print(fahr_to_cel(fahr))

