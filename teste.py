import time
import matplotlib.pyplot as plt

def busca_linear(lista, alvo):
    operacao = 0  # Contador de operações
    for i in range(len(lista)):
        operacao += 1  # Conta cada iteração do loop
        if lista[i] == alvo:
            return i, operacao  # Retorna a posição e o número de operações
    return -1, operacao  # Se não encontrar, retorna -1 e o número de operações

print()
# Melhor caso O(1)
numeros_pequenos = [15, 10, 5, 20, 25]
alvo = 15
inicio1 = time.perf_counter()
resultado, operacoes1 = busca_linear(numeros_pequenos, alvo)
fim1 = time.perf_counter()
tempo_execucao1 = fim1 - inicio1
print(f"Resultado(posição): {resultado}")
print(f"Tempo de execução: {tempo_execucao1:.6f} segundos")
print(f"Número total de operações: {operacoes1}\n")


# Médio caso O(n/2)
numeros_medios = list(range(1, 51))  # Lista de 1 a 50
alvo = 30
inicio2 = time.perf_counter()
resultado, operacoes2 = busca_linear(numeros_medios, alvo)
fim2 = time.perf_counter()
tempo_execucao2 = fim2 - inicio2
print(f"Resultado(posição): {resultado}")
print(f"Tempo de execução: {tempo_execucao2:.6f} segundos")
print(f"Número total de operações: {operacoes2}\n")


# Pior caso O(n)
numeros_grandes = list(range(1, 10001))  # Lista de 1 a 10000
alvo =1000
inicio3 = time.perf_counter()
resultado, operacoes3 = busca_linear(numeros_grandes, alvo)
fim3 = time.perf_counter()
tempo_execucao3 = fim3 - inicio3
print(f"Resultado(posição): {resultado}")
print(f"Tempo de execução: {tempo_execucao3:.6f} segundos")
print(f"Número total de operações: {operacoes3}\n")


# Pior caso O(n) (número não encontrado)
numeros_mega_grande = list(range(1, 1000001))  # Lista de 1 a 1000000
alvo = 1000001 
inicio4 = time.perf_counter()
resultado, operacoes4 = busca_linear(numeros_mega_grande, alvo)
fim4 = time.perf_counter()
tempo_execucao4 = fim4 - inicio4

if resultado != -1:
    print()
else:
    print(f"Tempo de execução: {tempo_execucao4:.6f} segundos")
    print(f"Resultado(posição): O número desejado não está na lista.")
    print(f"Número total de operações: {operacoes4}")



# Dados do melhor caso e caso médio
casos = ['Melhor Caso', 'Caso Médio','Pior caso']
tempos = [tempo_execucao1, tempo_execucao2,tempo_execucao3]  # Usando o tempo de execução para o melhor e caso médio
operacoes = [operacoes1, operacoes2,operacoes3]  # Usando o número de operações para o melhor e caso médio

# Criando o gráfico para tempo de execução
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(casos, tempos, color='lightcoral')
plt.title('Tempo de Execução por Caso')
plt.ylabel('Tempo')

# Criando o gráfico para número de operações
plt.subplot(1, 2, 2)
plt.bar(casos, operacoes, color='lightgreen')
plt.title('Número de Operações por Caso')
plt.ylabel('Número de Operações')

# Ajustando o layout
plt.tight_layout()
plt.show()
