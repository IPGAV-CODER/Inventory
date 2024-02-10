all_products = {}

def info_prod():
    prod  = str(input("Nome do produto: "))
    price = float(input("Preco: "))
    units = float(input("Unidades no estoque: "))
    all_products[prod] = [price, units]

while True:
    print('''

    1 - Novo Produto
    2 - Mostrar todos produtos
    3 - Consultar
    4 - Atualizar
    5 - Remover produto
    6 - Sair do programa

    ''')
    opcao = int(input("OPCAO: "))

    if opcao == 1:
        info_prod()
    elif opcao == 2:
        print(" =========== SISTEMA =============\n\n")
        for key, values in all_products.items():
            print(key, values)
    elif opcao == 3:
        print("procurar por")
        search_key = str(input("Encontre o produto: "))
        print(all_products[search_key])
    elif opcao == 4:
        print("Atualizar")
        search_key = str(input("Atualizar o produto: "))
        print(f"Atualizando {all_products[search_key]}")
        print("Formulario de atualizacao")
        info_prod()
    elif opcao == 5:
        search_key = str(input("Excluir o item: "))
        print(f"excluindo {all_products[search_key]}")
        del all_products[search_key]
        print(f"Item deletado {search_key}")
    elif opcao == 6:
        print("Saindo do programa. See You Later...")
        exit()
