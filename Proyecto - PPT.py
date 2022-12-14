import random
import getpass

options = ('Piedra', 'Papel', 'Tijeras')
userWins = 0
pcWins = 0
round = 1

def text():
    print(f'\nHas elegido: {options[user - 1]}')
    print(f'El PC a elegido: {options[pc - 1]}\n')

while True:

    print('\n---- Juego de Piedra. Papel, Tijeras ----')
    print('1 - Jugar. \n2 - Salir.')

    menuOption = int(input('Elige una opción: '))

    if menuOption == 1:
        while True:
            print(f'            ---- ROUND {round} ----')

            user = int(input('Ingresa: \n1 - Piedra. \n2 - Papel \n3 - Tijeras \n=> '))

            if not user in range(1, 4):
                    print('Esa opción no es válida. Ingresa nuevamente.')
                    continue

            pc = random.randint(1, 3)

            if pc == user:
                text()
                print('Empate')
                getpass.getpass('Presiona Enter para continuar')
            elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
                userWins += 1
                text()
                print('Has ganado la ronda!')
                getpass.getpass('Presiona Enter para continuar')
                if userWins == 2:
                    print('\nEres es el ganador final!')
                    getpass.getpass('Presiona Enter para regresar al menú')
                    break
            else:
                pcWins += 1
                text()
                print('Has perdido la ronda :c')
                getpass.getpass('Presiona Enter para continuar')
                if pcWins == 2:
                    print('\nLa PC es el ganador final!')
                    getpass.getpass('Presiona Enter para regresar al menú')
                    break
            round += 1
            print(f'\nMarcador => Usuario: {userWins} VS PC: {pcWins}')
    elif menuOption == 2:
        exit()
    else:
        print('Esa opción no es válida. Ingresa nuevamente')
        continue