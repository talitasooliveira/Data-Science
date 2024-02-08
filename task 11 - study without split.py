sentence_original = "This is a good task"

def alternate_upper_lower_caractere(sentence):
    result = []

    for i, caractere in enumerate(sentence):
        if i % 2 == 0:
            result.append(caractere.upper())  # Converte para maiúsculas se o índice for par
        else:
            result.append(caractere.lower())  # Converte para minúsculas se o índice for ímpar

    return ''.join(result)  # Une os caracteres de volta em uma string

sentence_alterada = alternate_upper_lower_caractere(sentence_original)
print(sentence_alterada)

def alternate_lower_upper_caractere(sentence):
    result = []

    for i, caractere in enumerate(sentence):
        if i % 2 == 0:
            result.append(caractere.lower())  # Converte para maiúsculas se o índice for par
        else:
            result.append(caractere.upper())  # Converte para minúsculas se o índice for ímpar

    return ''.join(result)  # Une os caracteres de volta em uma string

sentence_alterada1 = alternate_lower_upper_caractere(sentence_original)
print(sentence_alterada1)
