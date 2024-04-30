# Dados originais
dados = [
    [14, 23, 94],
    [15, 28, 97],
    [15, 20, 95],
    [16, 21, 108],
    [20, 22, 130],
    [15, 14, 102],
    [9, 21, 55],
    [9, 14, 59],
    [9, 21, 60],
    [11, 19, 72],
    [9, 17, 59],
    [13, 16, 81]
]

# Função para calcular valores normalizados
def normalizar_dados(dados):
    dados_normalizados = []
    for coluna in zip(*dados):
        min_valor = min(coluna)
        max_valor = max(coluna)
        coluna_normalizada = [(x - min_valor) / (max_valor - min_valor) for x in coluna]
        dados_normalizados.append(coluna_normalizada)
    return zip(*dados_normalizados)

# Normalizar os dados
dados_normalizados = normalizar_dados(dados)

# Imprimir os dados normalizados com colunas de tamanho fixo 25
for linha in dados_normalizados:
    for valor in linha:
        print("{:.8f}".format(valor).ljust(20), end="")
    print()

