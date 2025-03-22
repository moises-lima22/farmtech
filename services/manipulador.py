import csv
from models.cultura import criar_cultura

def inserir_cultura(culturas):
    tipo = input("\nDigite o tipo de cultura (cana ou milho): ").lower()
    if tipo == "cana":
        largura = float(input("Largura da area (m): "))
        comprimento = float(input("Comprimento da area (m): "))
        cultura = criar_cultura(tipo, {"largura": largura, "comprimento": comprimento})
    elif tipo == "milho":
        base = float(input("Base da area (m): "))
        altura = float(input("Altura da area (m): "))
        cultura = criar_cultura(tipo, {"base": base, "altura": altura})
    else:
        print("Tipo de cultura invalido!")
        return

    culturas.append(cultura)
    print("\nDados de plantio registrados com sucesso!")

def listar_culturas(culturas):
    print("\n========== CULTURAS ==========")
    if not culturas:
        print("Nenhuma cultura cadastrada.")
    for i, c in enumerate(culturas):
        unidade = "kg"
        print(f"\n[{i}] {c['tipo']} - Area: {c['total_area']} m² - Insumo Total: {c['total_insumo']} {unidade}")
        print(f"Descricao: {c['descricao']}")

def atualizar_cultura(culturas):
    listar_culturas(culturas)
    try:
        index = int(input("\nDigite o indice da cultura a ser atualizada: "))
        if 0 <= index < len(culturas):
            del culturas[index]
            print("Reinsira os dados da nova cultura:")
            inserir_cultura(culturas)
        else:
            print("Indice invalido.")
    except:
        print("Entrada invalida.")

def remover_cultura(culturas):
    listar_culturas(culturas)
    try:
        index = int(input("\nDigite o indice da cultura a ser removida: "))
        if 0 <= index < len(culturas):
            culturas.pop(index)
            print("Cultura removida com sucesso.")
        else:
            print("Indice invalido.")
    except:
        print("Entrada invalida.")

def exportar_para_csv(culturas):
    if not culturas:
        print("\nNenhum dado para exportar.")
        return

    with open("data/culturas.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
        campos = culturas[0].keys()
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(culturas)

    print("\nDados exportados com sucesso para 'data/culturas.csv'.")
