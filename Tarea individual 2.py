precio = float(input("precio original ($): "))
descuento = int (input ("Descuento (%): "))

final = precio * (1- descuento / 100)
# final = precio × (1 - descuento / 100)

print(f"Precio final ($) : ", final)

ahorro = precio * (descuento / 100)

print(f"se ahorra {ahorro} ($) ")