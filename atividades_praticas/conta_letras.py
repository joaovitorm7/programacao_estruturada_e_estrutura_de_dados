def conta_letra(string, letra):
    contagem = 0
    
    for caractere in string:
        if caractere == letra:
            contagem += 1
    
    return contagem

string = "desenvolvimento"
letra = "e"
resultado = conta_letra(string, letra)
print(resultado)  
