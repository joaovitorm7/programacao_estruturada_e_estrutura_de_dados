class medico:
    nome = ""
    codigo_crm = None

class paciente:
    nome = ""
    cpf = None
    bairro = ""
    rua = ""
    numero = None
    telefone = None

class atendimento:
    data = None

print("Escolha um dos itens abaixo\n")
pergunta = int(input("1 - Cadastrar Paciente\n 2 - Cadastrar Médico\n 3 - Cadastrar Atendimento\n 4 - Listar Atendimentos\n 5 - Encerrar"))

if(pergunta == 1):
    paciente



medicos = []
medico1 = medico()
medico1.nome = input('Digite o nome do médico: ')
medico1.codigo_crm = input('Digite o código de crm: ')
medicos.append(medico1)
print("O nome do médico é {} e seu número crm é {}".format(medico1.nome, medico1.codigo_crm))

medico2 = medico()
medico2.nome = input('Digite o nome do médico: ')
medico2.codigo_crm = input('Digite o código de crm: ')
medicos.append(medico2)
print("O nome do médico é {} e seu número crm é {}".format(medico2.nome, medico2.codigo_crm))


pacientes = []
paciente1 = paciente()
paciente1.nome = input('Digite o nome do paciente: ')
paciente1.cpf = input('Digite o cpf do paciente: ')
paciente1.bairro = input('Digite o bairro do paciente: ')
paciente1.rua = input('Digite a rua do paciente: ')
paciente1.numero = input('Digite o número do paciente: ')
paciente1.telefone = input('Digite o número do telefone do paciente: ')
pacientes.append(paciente1)
print("Dados do paciente: nome: {}, cpf: {}, bairro: {}, rua: {}, numero: {}, telefone: {}".format(paciente1.nome, paciente1.cpf, paciente1.bairro, paciente1.rua, paciente1.numero, paciente1.telefone))
