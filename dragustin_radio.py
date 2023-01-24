#Ejercicio Solicitar el valor del radio de un circulo para calcular su área y la circunferencia de un circulo de radio.
r = float(input("Escriba valor del radio: "))

area = 3.141592 * r ** 2

print("El area del circulo es igual a: {:.6f}".format(area))

circunferencia = 2 * 3.141592 * r

print("La circunferencia del circulo es igual a {:.6f}".format(circunferencia))
