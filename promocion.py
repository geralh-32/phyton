genero=  input("Ingrese la letra de su genero,Masculino(M),Femenino(F):")
edad=  int(input("Ingrese su edad:"))

if genero == "M" or "m" :
    pulsaciones=(210-edad)/10
    print(f"Cantidad de pulsaciones por segundo:{pulsaciones}")
if genero == "F" or "f" :
    pulsaciones=(220-edad)/10
    print(f"Cantidad de pulsaciones por segundo:{pulsaciones}")