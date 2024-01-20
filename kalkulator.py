#!/usr/bin/env python3

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
        return a / b

print("Kalkulator")
x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

wybor = input("Wybierz operację: ")

if wybor in ('1', '2', '3', '4'):

    if wybor == '1':
        print(f"{x} + {y} = {dodawanie(x, y)}")
    elif wybor == '2':
        print(f"{x} - {y} = {odejmowanie(x, y)}")
    elif wybor == '3':
        print(f"{x} * {y} = {mnozenie(x, y)}")
    elif wybor == '4':
        print(f"{x} / {y} = {dzielenie(x, y)}")
else:
    print("Nieprawidłowa operacja.")
