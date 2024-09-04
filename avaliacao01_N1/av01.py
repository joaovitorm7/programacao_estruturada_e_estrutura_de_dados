reservas = {
301: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 3, "hospede": "Ana Silva"},
302: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 2, "hospede": "Carlos Souza"},
303: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 1, "hospede": "Mariana Lima"},
304: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 5, "hospede": "João Pereira"},
305: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 4, "hospede": "Fernanda Costa"},
306: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 2, "hospede": "Ricardo Alves"},
307: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 1, "hospede": "Patrícia Gomes"},
308: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 3, "hospede": "Lucas Martins"},
309: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 4, "hospede": "Juliana Santos"},
310: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 2, "hospede": "Roberto Silva"},
311: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 1, "hospede": "Larissa Almeida"},
312: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 3, "hospede": "Eduardo Oliveira"},
}

# 01 Liste todos os quartos do tipo Suite com seus respectivos preços por noite.
for quarto in reservas:
    reserva = reservas[quarto]
    if reserva["tipo"] == "Suite":
        print(f"Quarto: {quarto}, Preço por noite: {reserva["preco_por_noite"]}")

# 02 Encontre o quarto com o maior valor total da reserva (preço por noite * número de noites reservadas).
maiorValorTotal_2 = 0
numeroDoquarto = None
for quarto in reservas:
    reserva = reservas[quarto]
    maiorValorTotal_1 = reserva["preco_por_noite"] * reserva["noites_reservadas"]
    if maiorValorTotal_2 < maiorValorTotal_1:
        maiorValorTotal_2 = maiorValorTotal_1
        numeroDoquarto = reserva["hospede"]
print(f"O quarto com o maior valor é de: {numeroDoquarto} e o seu preço é: {maiorValorTotal_2:.2f}")       

# 03 Calcule o valor total das reservas para cada tipo de quarto
totalSingle = 0
totalDouble = 0
totalSuite = 0

for quarto in reservas:
    reserva = reservas[quarto]
    reservasTotais = reserva["preco_por_noite"] * reserva["noites_reservadas"]

    if reserva["tipo"] == "Suite":
        totalSuite += reservasTotais
    elif reserva["tipo"] == "Single":
        totalSingle += reservasTotais
    elif reserva["tipo"] == "Double":
        totalDouble += reservasTotais

print(f"Total de reservas para quartos Single: R$ {totalSingle:.2f}")
print(f"Total de reservas para quartos Double: R$ {totalDouble:.2f}")
print(f"Total de reservas para quartos Suite: R$ {totalSuite:.2f}")

# 04 Crie um novo dicionário contendo apenas as reservas onde o valor total da reserva (preço por noite * número de noites reservadas) é maior que R$ 1000.00, com os respectivos IDs e nomes dos hóspedes.
novosQuartos = {}

print("Novo Dicionário: ")
for quarto in reservas:
    reserva = reservas[quarto]
    totalReserva = reserva["preco_por_noite"] * reserva["noites_reservadas"]
    if totalReserva >= 1000:
        novosQuartos[quarto] = {
            "Hospede": reserva["hospede"]
        }
print(novosQuartos)