def sumar(num1, num2):
  """Esta función suma dos números."""
  return num1 + num2

def restar(num1, num2):
  """Esta función resta el segundo número del primero."""
  return num1 - num2

def multiplicar(num1, num2):
  """Esta función multiplica dos números."""
  return num1 * num2

def dividir(num1, num2):
  """Esta función divide el primer número por el segundo."""
  if num2 == 0:
    return "¡Error! No se puede dividir por cero."
  else:
    return num1 / num2

def calculadora():
  """Esta función implementa la calculadora."""
  print("Selecciona la operación:")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")

  try:
    opcion = input("Ingresa el número de la operación que deseas realizar: ")

    if opcion in ('1', '2', '3', '4'):
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))

      if opcion == '1':
        resultado = sumar(num1, num2)
        print(f"{num1} + {num2} = {resultado}")
      elif opcion == '2':
        resultado = restar(num1, num2)
        print(f"{num1} - {num2} = {resultado}")
      elif opcion == '3':
        resultado = multiplicar(num1, num2)
        print(f"{num1} * {num2} = {resultado}")
      elif opcion == '4':
        resultado = dividir(num1, num2)
        print(f"{num1} / {num2} = {resultado}")
    else:
      print("Opción inválida. Por favor, elige una opción del 1 al 4.")

  except ValueError:
    print("Entrada inválida. Por favor, ingresa números.")

# Llamar a la función calculadora para iniciar el programa
if __name__ == "__main__":
  calculadora()