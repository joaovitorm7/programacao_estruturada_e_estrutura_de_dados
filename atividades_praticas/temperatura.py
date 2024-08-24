def processarDados(dados_sensores):
    cont_T = 0
    cont_P = 0
    cont_U = 0
    soma_T = 0
    soma_P = 0
    soma_U = 0

    tipo_leitura = ""
    valor_leitura = ""

    def processarLeitura(tipo, valor):
        if tipo == 'T':
            nonlocal cont_T, soma_T
            cont_T += 1
            soma_T += int(valor)
        elif tipo == 'P':
            nonlocal cont_P, soma_P
            cont_P += 1
            soma_P += int(valor)
        elif tipo == 'U':
            nonlocal cont_U, soma_U
            cont_U += 1
            soma_U += int(valor)

    for char in dados_sensores:
        if ('A' <= char <= 'Z'):
            tipo_leitura = char
            valor_leitura = ""
        elif '0' <= char <= '9':
            valor_leitura += char
        elif char == '|':
            if tipo_leitura and valor_leitura:
                processarLeitura(tipo_leitura, valor_leitura)

    return (cont_T, soma_T), (cont_P, soma_P), (cont_U, soma_U)


dados_sensores = "T25|P1013|U60|T24|T26|P1012|U65|U64|P1011|"
print(processarDados(dados_sensores))