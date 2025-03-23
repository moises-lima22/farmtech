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
            else:
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
        print(
            f"\n{cultura['tipo']} - Área: {cultura['total_area']} m² - Insumo Total: {cultura['total_insumo']} kg"
        )
        print(f"Descrição: {cultura['descricao']}")

        confirmacao = input("\nDeseja salvar esta cultura? (s/n): ").lower()
        if confirmacao == "s":
            culturas.append(cultura)
            print("✅ Cultura registrada com sucesso.")
        else:
            print("❌ Registro cancelado.")
        return
