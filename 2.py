nombre=input("Ingrese su nombre:")
edad=int(input("Ingrese su edad:"))

if edad >= 18 :
    print(f"{nombre}, Usted es mayor de edad")
else:
    print(f"{nombre}, Usted es menor de edad")
if edad <= 0 and edad > 100 :
    print(f"{nombre},Ingrese una edad válida")