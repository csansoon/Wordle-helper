from solver import WordleSolver
from colors import *

solver = WordleSolver()

fixed = ['','','','','']
wrong_position = [[],[],[],[],[]]
incorrect = []

for i in range(5):
    print(f'Escribe, si hay, la letra de color {green_fg}{green_bg}VERDE{reset} que tengas en esta posición.\n{gray}Si no hay ninguna letra simplemente pulsa ENTER.{reset}')
    for j in range(5):
        if (fixed[j] == ''):
            print(f'{gray_fg}{gray_bg} {reset}', end='')
        else:
            print(f'{green_fg}{green_bg}{fixed[j]}{reset}', end='')
    print(f'\n{" "*i}^')
    fixed[i] = input(f'> {green_bg}{green_fg}').upper()
    print(f'{reset}', end='\n' * 5)

for i in range(5):
    print(f'Escribe, si hay, todas las letras de color {yellow_fg}{yellow_bg}AMARILLO{reset} que tengas en esta posición.\n{gray}Escribe todas las letras seguidas, sin separación, y después pulsa enter. Si no hay ninguna letra simplemente pulsa ENTER.{reset}')
    for j in range(5):
        if (fixed[j] == ''):
            print(f'{gray_fg}{gray_bg} {reset}', end='')
        else:
            print(f'{green_fg}{green_bg}{fixed[j]}{reset}', end='')
    print(f'\n{" "*i}^')
    amarillas = input(f'> {yellow_fg}{yellow_bg}').upper()
    print(f'{reset}', end='\n' * 5)
    for letra in amarillas:
        wrong_position[i].append(letra)


print(f'Escribe, si hay, todas las letras de color {red_fg}{red_bg}ROJAS{reset} que tengas en el teclado.\n{gray}Las letras rojas son todas aquellas letras que has escrito pero no han aparecido ni en verde ni en amarillo, lo que significa que NO están en la palabra.{reset}')
rojas = input(f'> {red_fg}{red_bg}').upper()
print(f'{reset}', end='\n' * 5)
for letra in rojas:
    incorrect.append(letra)

count = input(f'Cuántas palabras quieres obtener? > ')

best_words = solver.find_best_word(fixed = fixed, wrong_position = wrong_position, incorrect = incorrect, count = 5)

print(f'Mejores palabras:', end=f'{reset}\n')
for word in best_words:
    print(word)