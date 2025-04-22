

try:
  numero_str = input("Ingresa un número entero: ")
  numero = int(numero_str)

  if numero % 2 == 0:
    print(f"El número {numero} es par.")
  else:
    print(f"El número {numero} es impar.")

except ValueError:
  print("Entrada inválida. Por favor, ingresa un número entero.")