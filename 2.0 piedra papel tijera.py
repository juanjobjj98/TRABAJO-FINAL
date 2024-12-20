import random  # Importamos la biblioteca para generar elecciones aleatorias.

# Lista de opciones para el juego.
opciones = ["Piedra", "Papel", "Tijera"]  # Cada índice representa una elección.

# Función para evaluar el resultado del juego.
def evaluar_resultado(jugador, computadora):
    """
    Determina el resultado del juego comparando las elecciones.
    """
    if jugador == computadora:
        return "Empate"
    elif (jugador == 0 and computadora == 2) or \
         (jugador == 1 and computadora == 0) or \
         (jugador == 2 and computadora == 1):  # Combinaciones en las que el jugador gana.
        return "¡Ganaste!"
    else:
        return "Perdiste"

# Iniciamos el bucle principal del juego.
while True:
    # Mostramos el menú al jugador.
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir del juego")

    # Capturamos y validamos la elección del jugador.
    try:
        jugador_eleccion = int(input("\nIngresa tu elección (1-4): "))
    except ValueError:  # Manejo de errores si el usuario no ingresa un número válido.
        print("⚠️ Por favor, ingresa un número válido (1-4).")
        continue

    # Verificamos si el jugador eligió salir.
    if jugador_eleccion == 4:
        print("👋 ¡Gracias por jugar! Hasta luego.")
        break

    # Validamos si la elección es válida (1, 2, o 3).
    if not (1 <= jugador_eleccion <= 3):  # Uso de operador lógico para validar rango.
        print("⚠️ Opción no válida. Intenta de nuevo.")
        continue

    # Ajustamos la elección del jugador al índice de la lista.
    jugador_eleccion -= 1

    # La computadora elige aleatoriamente.
    computadora_eleccion = random.randint(0, 2)

    # Mostramos las elecciones.
    print(f"\nTu elección: {opciones[jugador_eleccion]}")
    print(f"Elección de la computadora: {opciones[computadora_eleccion]}")

    # Evaluamos el resultado usando la función.
    resultado = evaluar_resultado(jugador_eleccion, computadora_eleccion)

    # Mensaje explicando el resultado.
    if resultado == "Empate":
        print("🤝 Resultado: ¡Es un empate!")
    elif resultado == "¡Ganaste!":
        print("🎉 Resultado: ¡Ganaste!")
    else:
        print("😞 Resultado: Perdiste")

    # Explicación adicional sobre las reglas.
    if jugador_eleccion == 0 and computadora_eleccion == 2:
        print("✔️ Piedra rompe Tijera")
    elif jugador_eleccion == 1 and computadora_eleccion == 0:
        print("✔️ Papel cubre Piedra")
    elif jugador_eleccion == 2 and computadora_eleccion == 1:
        print("✔️ Tijera corta Papel")
    elif computadora_eleccion == 0 and jugador_eleccion == 2:
        print("❌ Piedra rompe Tijera")
    elif computadora_eleccion == 1 and jugador_eleccion == 0:
        print("❌ Papel cubre Piedra")
    elif computadora_eleccion == 2 and jugador_eleccion == 1:
        print("❌ Tijera corta Papel")
