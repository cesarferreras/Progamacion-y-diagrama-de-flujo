def calcular_area_rectangulo():
  """Pide al usuario el largo y ancho de un rectángulo y muestra su área."""
  try:
    largo = float(input("Ingresa el largo del rectángulo: "))
    ancho = float(input("Ingresa el ancho del rectángulo: "))

    if largo < 0 or ancho < 0:
      print("Por favor, ingresa valores positivos para el largo y el ancho.")
    else:
      area = largo * ancho
      print(f"El área del rectángulo es: {area}")

  except ValueError:
    print("Entrada inválida. Por favor, ingresa números para el largo y el ancho.")

if __name__ == "__main__":
  calcular_area_rectangulo()