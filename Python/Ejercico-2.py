def celsius_a_fahrenheit():
  """Pide al usuario la temperatura en Celsius y muestra el equivalente en Fahrenheit."""
  try:
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
  except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para la temperatura.")

if __name__ == "__main__":
  celsius_a_fahrenheit()