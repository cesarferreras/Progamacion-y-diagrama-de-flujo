try:
  edad_str = input("Por favor, ingresa tu edad: ")
  edad = int(edad_str)

  if edad >= 18:
    print("Eres mayor de edad.")
  else:
    print("Eres menor de edad.")

except ValueError:
  print("Entrada inválida. Por favor, ingresa un número entero para la edad.")