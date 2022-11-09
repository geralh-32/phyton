tipopago=  ["Pago en efectivo","Pago con el celular","Tarjeta débito","Tarjeta crédito"]
cuenta=  int(input("Ingrese el monto de dinero que va a pagar:"))

if cuenta >= 600000 :
    print(f" Usted tiene las siguientes maneras de pagar: {tipopago[0]},{tipopago[1]},{tipopago[2]} y {tipopago[3]}")

if cuenta < 600000 and cuenta > 300000 :
    print(f" Usted tiene las siguientes maneras de pagar: {tipopago[0]},{tipopago[1]} y {tipopago[2]}")

if cuenta > 150000 and cuenta < 300000 :
     print(f" Usted tiene las siguientes maneras de pagar: {tipopago[0]} y {tipopago[1]}")

if cuenta < 15000 :
    print(f" Usted tiene la siguiente manera de pagar: {tipopago[0]}")