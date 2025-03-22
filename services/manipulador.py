import csv
import subprocess
from models.cultura import criar_cultura


def inserir_cultura(culturas):
    while True:
        tipo = input(
            "\nDigite o tipo de cultura (cana ou milho) ou 'x' para voltar: "
        ).lower()
        if tipo == "x":
            print("\n🔙 Retornando ao menu principal.")
            return

        if tipo not in ["cana", "milho"]:
            print("❌ Tipo de cultura inválido!")
            continue

        try:
            if tipo == "cana":
                largura = float(input("Largura da área (m): "))
                comprimento = float(input("Comprimento da área (m): "))
                if largura <= 0 or comprimento <= 0:
                    print("❌ Valores devem ser maiores que zero.")
                    return
                cultura = criar_cultura(
                    tipo, {"largura": largura, "comprimento": comprimento}
                )
            elif tipo == "milho":
                base = float(input("Base da área (m): "))
                altura = float(input("Altura da área (m): "))
                if base <= 0 or altura <= 0:
                    print("❌ Valores devem ser maiores que zero.")
                    return
                cultura = criar_cultura(tipo, {"base": base, "altura": altura})
        except ValueError:
            print("❌ Entrada inválida. Operação cancelada.")
            return

        print("\n📋 Visualização da cultura a ser registrada:")
        unidade = "kg"
        print(
            f"\n{cultura['tipo']} - Área: {cultura['total_area']} m² - Insumo Total: {cultura['total_insumo']} {unidade}"
        )
        print(f"Descrição: {cultura['descricao']}")

        confirmacao = input("\nDeseja salvar esta cultura? (s/n): ").lower()
        if confirmacao == "s":
            culturas.append(cultura)
            print("✅ Cultura registrada com sucesso.")
        else:
            print("❌ Registro cancelado.")
        return


def listar_culturas(culturas):
    print("\n========== 🌱 CULTURAS REGISTRADAS ==========\n")

    if not culturas:
        print("Nenhuma cultura cadastrada.")
    else:
        for i, c in enumerate(culturas):
            unidade = "kg"
            print(
                f"[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} {unidade}"
            )
            print(f"Descrição: {c['descricao']}")

    while True:
        escolha = input(
            "\n──────────────────────────────────────────────────────\n"
            "Digite [0] para voltar ao menu principal ou [1] para encerrar o sistema: "
        ).strip()
        if escolha == "0":
            return
        elif escolha == "1":
            print("Saindo do sistema...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")


def atualizar_cultura(culturas):
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return

    for i, c in enumerate(culturas):
        unidade = "kg"
        print(
            f"[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} {unidade}"
        )
        print(f"Descrição: {c['descricao']}")

    entrada = input(
        "\nDigite o índice da cultura a ser atualizada ou 'x' para cancelar: "
    ).strip()
    if entrada.lower() == "x":
        print("❌ Operação cancelada.")
        return

    try:
        index = int(entrada)
        if not (0 <= index < len(culturas)):
            print("❌ Índice inválido.")
            return

        cultura_original = culturas[index]
        tipo = cultura_original["tipo"]
        print(f"\n🔄 Atualizando cultura do tipo: {tipo}")

        if tipo == "cana":
            largura = input(f"Largura atual ({cultura_original['largura']} m): ")
            comprimento = input(
                f"Comprimento atual ({cultura_original['comprimento']} m): "
            )

            largura = float(largura) if largura.strip() else cultura_original["largura"]
            comprimento = (
                float(comprimento)
                if comprimento.strip()
                else cultura_original["comprimento"]
            )
            if largura <= 0 or comprimento <= 0:
                print("❌ Valores devem ser maiores que zero.")
                return

            cultura = criar_cultura(
                tipo, {"largura": largura, "comprimento": comprimento}
            )

        elif tipo == "milho":
            base = input(f"Base atual ({cultura_original['base']} m): ")
            altura = input(f"Altura atual ({cultura_original['altura']} m): ")

            base = float(base) if base.strip() else cultura_original["base"]
            altura = float(altura) if altura.strip() else cultura_original["altura"]
            if base <= 0 or altura <= 0:
                print("❌ Valores devem ser maiores que zero.")
                return

            cultura = criar_cultura(tipo, {"base": base, "altura": altura})

        print("\n📋 Visualização da cultura atualizada:")
        unidade = "kg"
        print(
            f"\n{cultura['tipo']} - Área: {cultura['total_area']} m² - Insumo Total: {cultura['total_insumo']} {unidade}"
        )
        print(f"Descrição: {cultura['descricao']}")

        confirmar = input("\nDeseja salvar esta atualização? (s/n): ").lower()
        if confirmar == "s":
            culturas[index] = cultura
            print("✅ Cultura atualizada com sucesso.")
        else:
            print("❌ Atualização cancelada.")

    except ValueError:
        print("❌ Entrada inválida.")


def remover_cultura(culturas):
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return

    for i, c in enumerate(culturas):
        unidade = "kg"
        print(
            f"[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} {unidade}"
        )
        print(f"Descrição: {c['descricao']}")

    entrada = input(
        "\nDigite o índice da cultura a ser removida ou 'x' para cancelar: "
    ).strip()
    if entrada.lower() == "x":
        print("❌ Operação cancelada.")
        return

    try:
        index = int(entrada)
        if 0 <= index < len(culturas):
            confirmacao = input(
                "Tem certeza que deseja remover esta cultura? (s/n): "
            ).lower()
            if confirmacao == "s":
                culturas.pop(index)
                print("✅ Cultura removida com sucesso.")
            else:
                print("❌ Operação cancelada.")
        else:
            print("❌ Índice inválido.")
    except ValueError:
        print("❌ Entrada inválida.")


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


def executar_analise_r():
    try:
        subprocess.run(["Rscript", "r_scripts/analise.R"], check=True)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o script R:", e)
        return

    while True:
        escolha = input(
            "\nDigite [0] para voltar ao menu principal ou [1] para encerrar o sistema: "
        ).strip()
        if escolha == "0":
            return
        elif escolha == "1":
            print("Saindo do sistema...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
