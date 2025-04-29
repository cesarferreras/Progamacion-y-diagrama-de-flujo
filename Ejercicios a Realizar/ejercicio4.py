

import math

def calculadora_avanzada():
  """Calculadora que utiliza la biblioteca math."""
  print("Calculadora Avanzada")
  print("Selecciona la operación:")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Potencia (a^b)")
  print("6. Raíz cuadrada")
  print("7. Logaritmo natural (ln)")
  print("8. Seno")
  print("9. Coseno")
  print("10. Tangente")

  try:
    opcion = input("Ingresa el número de la operación que deseas realizar: ")

    if opcion in ('1', '2', '3', '4'):
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
      if opcion == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
      elif opcion == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
      elif opcion == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
      elif opcion == '4':
        if num2 == 0:
          print("¡Error! No se puede dividir por cero.")
        else:
          print(f"{num1} / {num2} = {num1 / num2}")
    elif opcion == '5':
      base = float(input("Ingresa la base: "))
      exponente = float(input("Ingresa el exponente: "))
      print(f"{base}^{exponente} = {math.pow(base, exponente)}")
    elif opcion == '6':
      num = float(input("Ingresa el número: "))
      if num >= 0:
        print(f"La raíz cuadrada de {num} es: {math.sqrt(num)}")
      else:
        print("¡Error! No se puede calcular la raíz cuadrada de un número negativo.")
    elif opcion == '7':
      num = float(input("Ingresa el número: "))
      if num > 0:
        print(f"El logaritmo natural de {num} es: {math.log(num)}")
      else:
        print("¡Error! No se puede calcular el logaritmo de un número no positivo.")
    elif opcion in ('8', '9', '10'):
      angulo_grados = float(input("Ingresa el ángulo en grados: "))
      angulo_radianes = math.radians(angulo_grados)
      if opcion == '8':
        print(f"El seno de {angulo_grados} grados es: {math.sin(angulo_radianes)}")
      elif opcion == '9':
        print(f"El coseno de {angulo_grados} grados es: {math.cos(angulo_radianes)}")
      elif opcion == '10':
        print(f"La tangente de {angulo_grados} grados es: {math.tan(angulo_radianes)}")
    else:
      print("Opción inválida.")

  except ValueError:
    print("Entrada inválida. Por favor, ingresa números.")

if __name__ == "__main__":
  calculadora_avanzada()