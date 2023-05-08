import random

# Definir los participantes
num_participantes = 16
participantes = []
for i in range(num_participantes):
    nombre = input("Ingrese el nombre del participante {}: ".format(i+1))
    participantes.append(nombre)

# Generar los enfrentamientos para la primera ronda
random.shuffle(participantes)
enfrentamientos = []
print('\n-- Enfrentamientos de la ronda 1 --')
for i in range(0, len(participantes), 2):
    enfrentamiento = (participantes[i], participantes[i+1])
    enfrentamientos.append(enfrentamiento)
    print('{} vs. {}'.format(participantes[i], participantes[i+1]))
enfrentamientos = enfrentamientos[:8]  # Solo los primeros cuatro enfrentamientos

# Definir la función para jugar una partida
def jugar_partida(jugador1, jugador2):
    resultado = input('Ingrese el resultado de la partida entre {} y {}: '.format(jugador1, jugador2))
    return jugador1 if resultado == '1' else jugador2

# Realizar las rondas sucesivas hasta que quede un solo ganador
ronda = 1
while len(participantes) > 1 and ronda <= 4:
    print('\n\n------ RONDA {} ------'.format(ronda))
    ganadores = []
    for enfrentamiento in enfrentamientos:
        jugador1, jugador2 = enfrentamiento
        ganador = jugar_partida(jugador1, jugador2)
        ganadores.append(ganador)
    participantes = ganadores
    enfrentamientos = []
    if ronda < 4:
        print('\n-- Enfrentamientos de la ronda {} --'.format(ronda+1))
        for i in range(0, len(participantes), 2):
            enfrentamiento = (participantes[i], participantes[i+1])
            enfrentamientos.append(enfrentamiento)
            print('{} vs. {}'.format(participantes[i], participantes[i+1]))
        enfrentamientos = enfrentamientos[:4]  # Solo los primeros cuatro enfrentamientos
    ronda += 1

# Mostrar al ganador final
print('\n\nEl ganador del torneo es {}!'.format(participantes[0]))
