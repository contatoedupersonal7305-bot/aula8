import json

def carregar_produtos():
    try:
        arquivo = open("produtos.json", "r", encoding="utf-8")
        produtos = json.load(arquivo)
        arquivo.close()
        return produtos
    except FileNotFoundError:
        return []

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

produtos = carregar_produtos()

def pesquisa_id():
    escolha = int(input("Qual o ID que deseja ver? : "))
    encontrou = False

    for produto in produtos:
        if produto["id"] == escolha:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | Estoque: {produto['estoque']}")
            encontrou = True
            break
            
    if not encontrou:
        print("Produto não encontrado!")
    
def pesquisa_estoque():
    limite = int(input("Mostrar produtos com estoque abaixo de: "))
    encontrou = False

    print(f"\n--- PRODUTOS COM ESTOQUE ABAIXO DE {limite} ---")
    for produto in produtos:
        if produto["estoque"] < limite:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | Estoque: {produto['estoque']}")
            encontrou = True
            
    if not encontrou:
        print("Nenhum produto encontrado abaixo dessa quantidade.")
def mostrar_produtos():
    print("\n----- LISTA DE PRODUTOS -----")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for p in produtos:
            print(p)

def cadastrar_produto():
    id = int(input("Qual o ID do Produto? "))
    nome = input("Qual o Nome do Produto? ")
    categoria = input("Qual a Categoria do Produto? ")
    preco = float(input("Qual o Preço do Produto? "))
    estoque = int(input("Qual a Quantidade em Estoque do Produto? "))

    novo = {"id": id, "nome": nome, "categoria": categoria, "preco": preco, "estoque": estoque}

    produtos.append(novo)
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")

def remover_produto():
    print("\n----- REMOVER PRODUTO -----")
    id_remover = int(input("Digite o ID do produto que deseja remover: "))
    
    global produtos
    nova_lista = []
    removido = False

    for p in produtos:
        if p["id"] != id_remover:
            nova_lista.append(p)
        else:
            removido = True

    if removido:
        produtos = nova_lista
        salvar_produtos(produtos)
        print("Produto removido com sucesso!")
    else:
        print("ID não encontrado no estoque.")

def consultar_dados():
    total_produtos = len(produtos)
    print(f"\nTotal de produtos cadastrados no sistema: {total_produtos}")
    
    print("\n--- ALERTAS DE ESTOQUE BAIXO (<= 10) ---")
    tem_baixo = False
    for produto in produtos:
        if produto["estoque"] <= 10:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Estoque Atual: {produto['estoque']}")
            tem_baixo = True
            
    if not tem_baixo:
        print("Nenhum produto com estoque baixo no momento.")

while True:
    print("\n-----CONTROLE DE ESTOQUE-----")
    print("01 - PESQUISA POR ID")
    print("02 - PESQUISA POR ESTOQUE")
    print("03 - MOSTRAR ESTOQUE")
    print("04 - CADASTRAR PRODUTO")
    print("05 - REMOVER PRODUTO")
    print("06 - CONSULTAR DADOS (Resumo & Alertas)")
    print("07 - SAIR")

    pergunta = int(input("Qual opção deseja? "))

    if pergunta == 1:
        pesquisa_id()
    elif pergunta == 2:
        pesquisa_estoque()
    elif pergunta == 3:
        mostrar_produtos()
    elif pergunta == 4:
        cadastrar_produto()
    elif pergunta == 5:
        remover_produto()
    elif pergunta == 6:
        consultar_dados()
    elif pergunta == 7:
        print("Programa Finalizado! Até a Próxima...")
        break
    else:
        print("Opção Inválida, tente novamente")