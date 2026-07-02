def exibir_linha():
    print("=" * 25)


def exibir_menu():
    print()
    exibir_linha()
    print("AVEDEX - MENU PRINCIPAL")
    exibir_linha()
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Listar aves")
    print("3 - Ver detalhes de uma ave (por ID)")
    print("4 - Buscar ave por nome")  # <-- Nova opção adicionada
    print("5 - Sobre a AveDex")        # <-- Mudou de 4 para 5
    print("0 - Sair")


def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")


def listar_aves(catalogo):
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave
    return None


def exibir_detalhes(ave):
    print()
    exibir_linha()
    print("DETALHES DA AVE")
    exibir_linha()

    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave['curiosidade']}")


def buscar_aves_por_nome(catalogo, termo_busca):
    resultados = []
    termo_busca_lower = termo_busca.lower()
    
    for ave in catalogo:
        nome = ave["nome_popular"].lower()
        if termo_busca_lower in nome:
            resultados.append(ave)
    return resultados


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves.")
    print("O projeto evolui durante a disciplina de Boas Práticas.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas e cidades",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto lembra a expressão bem-te-vi."
    },
    {
        "id": 2,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas rurais",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "O macho possui plumagem amarela intensa."
    },
    {
        "id": 3,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e pequenos invertebrados",
        "curiosidade": "Constrói ninhos de barro."
    },
    {
        "id": 4,
        "nome_popular": "Arara-azul",
        "nome_cientifico": "Anodorhynchus hyacinthinus",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Granívora",  
        "habitat": "Pantanal e Cerrado",
        "alimentacao": "Frutos e sementes",
        "curiosidade": "É uma das maiores araras do mundo."
    },
    {
        "id": 5,
        "nome_popular": "Tucano-toco",
        "nome_cientifico": "Ramphastos toco",
        "ordem": "Piciformes",
        "familia": "Ramphastidae",
        "dieta_tipo": "Onívora",     
        "habitat": "Florestas e Cerrado",
        "alimentacao": "Frutas, ovos e pequenos animais",
        "curiosidade": "Possui um bico que pode chegar a 20 cm."
    }
]

print("=" * 50)
print("AVEDEX")
print("=" * 50)

nome_usuario = input("Digite seu nome: ").strip()

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()

    opcao_menu = input("Escolha uma opção: ").strip()

    print()

    if opcao_menu == "1":
        mostrar_boas_vindas(nome_usuario)

    elif opcao_menu == "2":
        listar_aves(catalogo_aves)

    elif opcao_menu == "3":
        listar_aves(catalogo_aves)

        codigo_escolhido = input(
            "\nDigite o código da ave: "
        ).strip()

        ave_encontrada = buscar_ave_por_id(
            catalogo_aves,
            codigo_escolhido
        )

        if ave_encontrada is not None:
            exibir_detalhes(ave_encontrada)
        else:
            print("Ave não encontrada.")

    elif opcao_menu == "4":  
        termo = input("Digite o nome (ou parte do nome) da ave: ").strip()
        aves_encontradas = buscar_aves_por_nome(catalogo_aves, termo)
        
        if len(aves_encontradas) > 0:
            print(f"\nAve(s) encontrada(s) com o termo '{termo}':")
            for ave in aves_encontradas:
                exibir_detalhes(ave)
        else:
            print(f"Nenhuma ave encontrada com o termo '{termo}'.")

    elif opcao_menu == "5":  # <-- Mudou de 4 para 5
        mostrar_sobre()

    elif opcao_menu == "0":
        print("Encerrando a AveDex.")
        print(f"Até logo, {nome_usuario}!")

    else:
        # Atualizado para incluir o número 5
        print("Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5.")

    if opcao_menu != "0":
        pausar()

resultados_teste = buscar_aves_por_nome(catalogo_aves,"barro")
print(resultados_teste)