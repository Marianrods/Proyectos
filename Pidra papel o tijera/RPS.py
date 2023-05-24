# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from collections import defaultdict

def player(prev_play, opponent_history=[]):
    # Diccionario para almacenar las estadísticas de movimientos del oponente
    estadisticas = defaultdict(lambda: {'R': 0, 'P': 0, 'S': 0})

    # Agregar el último movimiento del oponente al historial
    if prev_play in ['R', 'P', 'S']:
        opponent_history.append(prev_play)

    # Movimiento predeterminado
    eleccion = 'R'

    if len(opponent_history) >= 2:
        # Obtener los dos últimos movimientos del oponente
        ultimos_dos_movimientos = opponent_history[-2:]

        # Incrementar el contador correspondiente a la combinación de movimientos
        estadisticas[ultimos_dos_movimientos[0]][ultimos_dos_movimientos[1]] += 1

        # Predecir el próximo movimiento basado en las estadísticas
        movimiento_predicho = max(estadisticas[ultimos_dos_movimientos[0]], key=estadisticas[ultimos_dos_movimientos[0]].get)

        # Asignar el movimiento que vence al movimiento predicho del oponente
        if movimiento_predicho == 'R':
            eleccion = 'P'
        elif movimiento_predicho == 'P':
            eleccion = 'S'
        elif movimiento_predicho == 'S':
            eleccion = 'R'

    return eleccion







