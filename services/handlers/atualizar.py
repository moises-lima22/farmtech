from models.cultura import criar_cultura


def atualizar_cultura(culturas):
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return

    for i, c in enumerate(culturas):
        print(
            f"[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} kg"
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

        original = culturas[index]
        tipo = original["tipo"]
        print(f"\n🔄 Atualizando cultura do tipo: {tipo}")

        if tipo == "cana":
            largura = input(f"Largura atual ({original['largura']} m): ")
            comprimento = input(f"Comprimento atual ({original['comprimento']} m): ")

            largura = float(largura) if largura.strip() else original["largura"]
            comprimento = (
                float(comprimento) if comprimento.strip() else original["comprimento"]
            )
            if largura <= 0 or comprimento <= 0:
                print("❌ Valores devem ser maiores que zero.")
                return
            cultura = criar_cultura(
                tipo, {"largura": largura, "comprimento": comprimento}
            )

        else:
            base = input(f"Base atual ({original['base']} m): ")
            altura = input(f"Altura atual ({original['altura']} m): ")

            base = float(base) if base.strip() else original["base"]
            altura = float(altura) if altura.strip() else original["altura"]
            if base <= 0 or altura <= 0:
                print("❌ Valores devem ser maiores que zero.")
                return
            cultura = criar_cultura(tipo, {"base": base, "altura": altura})

        print("\n📋 Visualização da cultura atualizada:")
        print(
            f"\n{cultura['tipo']} - Área: {cultura['total_area']} m² - Insumo Total: {cultura['total_insumo']} kg"
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
