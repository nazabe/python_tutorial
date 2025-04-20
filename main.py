print("Hello, World!")

x = 5
y = "John"

print(21 % 5)

print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

snake_case = "is used in linux kernel, on c code"

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

import random

print(random.randrange(1, 10))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

a = "Hello, World!"
print(a[0:8])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

i = 1
while i < 6:
  print(i)
  i += 1

# first comments on python

# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Imprimir cuadrado, rectangulo, triangulo, puente
# Imprimir numeros pares e impares

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

edad = int(input("Ingrese su edad: "))
print(f"Tenés {edad} años")