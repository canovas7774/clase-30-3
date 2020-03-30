cantidad = float(input(" cuanto queres inventir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
for i in range(años):
    cantidad *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))50