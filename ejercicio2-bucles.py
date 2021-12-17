#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

x = 1
print("¿Cual es tu edad?")
edad = int(input())
while (x<edad):
    print(x)
    x = x+1
print(x)
