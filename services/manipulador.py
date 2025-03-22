from models.cultura import criar_cultura

def inserir_cultura(culturas):
    tipo = input("\nDigite o tipo de cultura (Café ou Milho): ")
    if tipo.lower() == "café":
        largura = float(input("Largura (m): "))
        comprimento = float(input("Comprimento (m): "))
        ruas = int(input("Quantidade de ruas: "))
        cultura = criar_cultura(tipo, {"largura": largura, "comprimento": comprimento}, ruas)
    elif tipo.lower() == "milho":
        base = float(input("Base (m): "))
        altura = float(input("Altura (m): "))
        cultura = criar_cultura(tipo, {"base": base, "altura": altura})
    else:
        print("Tipo de cultura inválido!")
        return

    culturas.append(cultura)
    print("\nCultura adicionada com sucesso!")

def listar_culturas(culturas):
    print("\n========== CULTURAS ==========")
    if not culturas:
        print("Nenhuma cultura cadastrada.")
    for i, c in enumerate(culturas):
        print(f"\n[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} {'mL' if c['tipo'] == 'Café' else 'kg'}")

def atualizar_cultura(culturas):
    listar_culturas(culturas)
    try:
        index = int(input("\nDigite o índice da cultura a ser atualizada: "))
        if 0 <= index < len(culturas):
            del culturas[index]
            print("Reinsira os dados da nova cultura:")
            inserir_cultura(culturas)
        else:
            print("Índice inválido.")
    except:
        print("Entrada inválida.")

def remover_cultura(culturas):
    listar_culturas(culturas)
    try:
        index = int(input("\nDigite o índice da cultura a ser removida: "))
        if 0 <= index < len(culturas):
            culturas.pop(index)
            print("Cultura removida com sucesso.")
        else:
            print("Índice inválido.")
    except:
        print("Entrada inválida.")
