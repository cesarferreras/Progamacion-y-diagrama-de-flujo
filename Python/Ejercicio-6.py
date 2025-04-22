def realizar_operaciones():
  """Pide dos números al usuario y muestra su suma, resta, multiplicación y división."""
  try:
    num1_str = input("Ingresa el primer número: ")
    num1 = float(num1_str)

    num2_str = input("Ingresa el segundo número: ")
    num2 = float(num2_str)

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    if num2 == 0:
      division = "No se puede dividir por cero."
    else:
      division = num1 / num2

    print(f"La suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    print(f"La división de {num1} entre {num2} es: {division}")

  except ValueError:
    print("Entrada inválida. Por favor, ingresa números.")

if __name__ == "__main__":
  realizar_operaciones()
