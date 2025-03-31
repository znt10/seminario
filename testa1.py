def busca_linear(lista,alvo):
    indici = []
    for a in range(len(lista)):
        if lista[a] == alvo:
            indici.append(a)
            
    return indici
    
lista = [10, 30, 40, 66, 234, 45, 87, 23, 56, 78, 90, 12, 34, 67, 89, 100, 11,
22, 33, 44, 55, 66, 77, 88, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295,10]

alvo = 10
resultado = busca_linear(lista,alvo)

if resultado:
    print(f"Elemento encontrado nas posições: {resultado}")
else:
    print("Elemento não encontrado.")