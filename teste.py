def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i 
    return -1



numeros_pequenos = [15, 10, 5, 20, 25]
alvo = 15
resultado = busca_linear(numeros_pequenos, alvo)
print(f"Resultado: {resultado}")



numeros_medios = list(range(1, 51))  # Lista de 1 a 50
alvo = 30
resultado = busca_linear(numeros_medios, alvo)
print(f"Resultado: {resultado}")




numeros_grandes = list(range(1, 1001))  # Lista de 1 a 1000
alvo = 999
resultado = busca_linear(numeros_grandes, alvo)
print(f"Resultado: {resultado}")


numeros_mega_grande = list(range(1, 100001))  # Lista de 1 a 100000
alvo = 100001  # Valor que não está na lista
resultado = busca_linear(numeros_mega_grande, alvo)

if resultado != -1:
    print()
else:
    print('O numero dejesado nao contem na lista')
