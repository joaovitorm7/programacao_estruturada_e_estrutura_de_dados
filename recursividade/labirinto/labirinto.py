def resolver_labirinto(labirinto, entrada, saida):
    visitados = [[False for _ in range(len(labirinto[0]))] for _ in range(len(labirinto))]
    
    return busca_caminho(labirinto, entrada[0], entrada[1], saida[0], saida[1], visitados)

def busca_caminho(labirinto, x, y, saida_x, saida_y, visitados):
    if x < 0 or x >= len(labirinto) or y < 0 or y >= len(labirinto[0]):
        return False
    
    if x == saida_x and y == saida_y:
        return True
    
    if labirinto[x][y] == 1 or visitados[x][y]:
        return False
    
    visitados[x][y] = True
    
    if busca_caminho(labirinto, x-1, y, saida_x, saida_y, visitados):
        return True
    
    if busca_caminho(labirinto, x+1, y, saida_x, saida_y, visitados):
        return True
    
    if busca_caminho(labirinto, x, y-1, saida_x, saida_y, visitados):
        return True
    
    if busca_caminho(labirinto, x, y+1, saida_x, saida_y, visitados):
        return True
    
    return False

def obter_coordenadas(mensagem, limite_linhas, limite_colunas):
    while True:
        try:
            linha, coluna = map(int, input(mensagem).split())
            if 0 <= linha < limite_linhas and 0 <= coluna < limite_colunas:
                return (linha, coluna)
            else:
                print(f"As coordenadas devem estar entre 0 e {limite_linhas - 1} para as linhas e 0 e {limite_colunas - 1} para as colunas.")
        except ValueError:
            print("Entrada inválida. Por favor, insira dois números inteiros separados por espaço.")

labirinto = [
   [0, 1, 0, 0, 0],
   [0, 1, 0, 1, 0],
   [0, 0, 0, 1, 0],
   [0, 1, 1, 1, 0],
   [0, 0, 0, 0, 0]
]

entrada = obter_coordenadas("Digite as coordenadas da entrada (linha coluna) ex.: 0 1: ", len(labirinto), len(labirinto[0]))
saida = obter_coordenadas("Digite as coordenadas da saída (linha coluna) ex.: 1 2: ", len(labirinto), len(labirinto[0]))

if resolver_labirinto(labirinto, entrada, saida):
    print("Existe um caminho!")
else:
    print("Não existe caminho.")
