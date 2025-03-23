import csv


def exportar_para_csv(culturas):
    if not culturas:
        print("\nNenhum dado para exportar.")
        return

    campos = [
        "tipo",
        "descricao",
        "formato_area",
        "largura",
        "comprimento",
        "base",
        "altura",
        "insumo",
        "quantidade_insumo",
        "total_area",
        "total_insumo",
    ]

    with open(
        "data/culturas.csv", mode="w", newline="", encoding="utf-8"
    ) as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writeheader()
        for cultura in culturas:
            linha = {campo: cultura.get(campo, None) for campo in campos}
            escritor.writerow(linha)

    print("\n📁 Dados exportados com sucesso para 'data/culturas.csv'.")
