import sys

# Crear un script llamado aprobado.py que realice lo siguiente:

# Debe tomar 2 argumentos, ambos números enteros del 0 al 10, sino, mostrar un error.
# Si ambos valores son mayores o igual a 7 devolver imprimir “Promocionado”
# Si ambos valores son mayor o igual a 4 imprimir “Aprobado, debe rendir final”
# Si uno de los dos valores es menor a 4 imprimir “Desaprobado, debe recuperar el primer parcial” 
# (Si el primer argumento es 3 debe recuperar el primer parcial, si no, debe decir lo mismo pero 
# con segundo parcial)
# Si ambos argumentos son menores a 4 debe imprimir “Desaprobó ambos parciales, debe recursar”
# En caso de no mostrar uno o ambos argumentos debe mostrar información de como usar el script.

if len(sys.argv) != 3:
    print("error, necesito 2 argumentos")
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])
        
        
if sys.argv[] != int and (sys.argv[] > 10 or sys.argv[] < 0):
    print ("Error, ingrese dos numeros enteros entre 0 y 10")
elif sys.argv[1] > 7 and sys.argv[2] > 7:
    print ("Promocionado")
elif sys.argv[1] >= 4 and sys.argv[2] >= 4:
    print ("Aprobado, debe rendir final")
elif sys.argv[1] < 4 or sys.argv[2] < 4:
    if sys.argv[1] == 3:
        print ("Debe recuperar el primer parcial")
        else: ("Desaprobo ambos parciales, debe recursar") 
elif sys.argv[1] == () or sys.argv[2] == ():
    print ("Usted no ingreso uno o ninguno de los valores, debe ingresar dos numeros enteros, entre 0 y 10")
    