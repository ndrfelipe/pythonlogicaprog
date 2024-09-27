print("Sistema de Cadastro de Clientes\n")
print("Escolha as opções: \n")
print("Adicionar um novo cliente: (1) ")
print("Exibir clientes: (2) ")
print("Buscar cliente pelo nome: (3)")
print("Atualizar informações de um cliente: (4)")
print("Excluir um cliente do sistema: (5)")
print("Sair (6) \n")

opcao = int(input("Qual serviço você deseja?"))

match(opcao):
    case 1:
        print("Cliente adicionado.")
    case 2:
        print("Lista de clientes exibidos")
    case 3:
        print("Cliente buscado pelo nome")
    case 4:
        print("Informações atualizadas")
    case 5:
        print("Cliente excluido")
    case 6:
        print("Saindo do sistema")
    case __:
        print('numero inválido')