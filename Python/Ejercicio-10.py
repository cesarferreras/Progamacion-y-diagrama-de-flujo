suma = 0
print("Ingresa números para sumar (ingresa 0 para detener):")

while True:
  try:
    entrada = input("Ingresa un número: ")
    numero = float(entrada)
    if numero == 0:
      break  # Sale del bucle si el usuario ingresa 0
    suma += numero
  except ValueError:
    print("Entrada inválida. Por favor, ingresa un número.")

print(f"La suma total de los números ingresados es: {suma}")
