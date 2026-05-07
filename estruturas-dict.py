def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador_char = dict()
    index = 1
#TODO: Itere através de cada caractere na string string.
    for char in string:
        
        if char not in contador_char:
            contador_char.setdefault(char, index)
        
        else:
            contador_char.update({char : index+1})

#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
    
    return contador_char

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)