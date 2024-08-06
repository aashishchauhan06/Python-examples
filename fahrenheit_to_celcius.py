#!/usr/bin/python3

def fahr_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

fahr = int(input('Enter temperature in Fahrenheit please: '))

try:
    print(fahr_to_cel(fahr))
except ValueError as ex:
      exit("I am sorry. Only real numbers are allowed")
    

