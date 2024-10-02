def max_vogais_consecutivas(texto):
    vogais = "aeiouAEIOU"
    max_contagem = contagem_atual = 0

    for char in texto:
        contagem_atual = contagem_atual + 1 if char in vogais else 0
        max_contagem = max(max_contagem, contagem_atual)

    return max_contagem

# Exemplos de uso
print(max_vogais_consecutivas("abacate"))  # Saída: 0
print(max_vogais_consecutivas("beautiful day"))  # Saída: 3
print(max_vogais_consecutivas(""))  # Saída: 0
