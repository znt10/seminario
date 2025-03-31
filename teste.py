import time

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i 
    return -1


#melhor caso O(1)
numeros_pequenos = [15, 10, 5, 20, 25]
alvo = 15
inicio1 = time.perf_counter()
resultado = busca_linear(numeros_pequenos, alvo)
fim1 = time.perf_counter()
print(f"Resultado: {resultado}")
tempo_execucao1 = fim1 -inicio1
print(f"Tempo de execução: {tempo_execucao1:.6f} segundos")

print()
#medio caso O(n)
numeros_medios = list(range(1, 51))  # Lista de 1 a 50
alvo = 30
inicio2 = time.perf_counter()
resultado = busca_linear(numeros_medios, alvo)
fim2 = time.perf_counter()
print(f"Resultado: {resultado}")
tempo_execucao2 = fim2 -inicio2
print(f"Tempo de execução: {tempo_execucao2:.6f} segundos")
print()

#pior caso O(n)
numeros_grandes = list(range(1, 10000))  # Lista de 1 a 1000
alvo = 9999
inicio3 = time.perf_counter()
resultado = busca_linear(numeros_grandes, alvo)
fim3 = time.perf_counter()
print(f"Resultado: {resultado}")
tempo_execucao3 = fim3 -inicio3
print(f"Tempo de execução: {tempo_execucao3:.6f} segundos")
print()

#pior caso O(n)
numeros_mega_grande = list(range(1, 1000000))  # Lista de 1 a 100000
alvo = 1000001
inicio4 = time.perf_counter()
resultado = busca_linear(numeros_mega_grande, alvo)
fim4 = time.perf_counter()
tempo_execucao4 = fim4 - inicio4
if resultado != -1:
    print()
else:
    print(f"Tempo de execução: {tempo_execucao3:.6f} segundos")
    print('O numero dejesado nao contem na lista')
    

