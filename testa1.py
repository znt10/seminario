import matplotlib.pyplot as plt

# Dados dos melhores e piores casos
casos = ['Melhor Caso', 'Pior Caso']
tempos = [tempo_execucao1, tempo_execucao3]  # Usando o tempo de execução para o melhor e pior caso
operacoes = [operacoes1, operacoes3]  # Usando o número de operações para o melhor e pior caso

# Criando o gráfico para tempo de execução
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(casos, tempos, color='lightcoral')
plt.title('Tempo de Execução por Caso')
plt.ylabel('Tempo (segundos)')

# Criando o gráfico para número de operações
plt.subplot(1, 2, 2)
plt.bar(casos, operacoes, color='lightgreen')
plt.title('Número de Operações por Caso')
plt.ylabel('Número de Operações')

# Ajustando o layout
plt.tight_layout()
plt.show()
