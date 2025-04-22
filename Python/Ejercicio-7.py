

try:
  numero_str = input("Ingresa un número: ")
  numero = float(numero_str)

  if numero > 0:
    print("El número es positivo.")
  elif numero < 0:
    print("El número es negativo.")
  else:
    print("El número es cero.")

except ValueError:
  print("Entrada inválida. Por favor, ingresa un número.")