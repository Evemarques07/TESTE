#1_______________________________________________________________________________

# total_notas = 0
# soma_notas = 0
# contador = 0

# while contador < 4:
#     nota = float(input("Digite uma nota de 0 a 10: "))

#     if nota < 0 and nota > 10:
#         break
#     else:
#         soma_notas += nota
#         total_notas += 1
#         contador +=1

# media = soma_notas / total_notas

# print(f"A média das notas é {media}")

#2_________________________________________________________________________________

# total_notas = 0
# soma_notas = 0
# while True:
#     nota = float(input("Digite uma nota de 0 a 10: "))
#     if nota < 0:
#         break
#     else:
#         soma_notas += nota
#         total_notas += 1
# media = soma_notas / total_notas
# print(f"A média das notas é {media}")

#3_________________________________________________________________________________

n = int(input("Digite um número: "))
resultado = 1

for i in range(1, n + 1):
    resultado *= i

print(f'O fatorial de {n} é {resultado}')

#4__________________________________________________________________________________

