def remover_cultura(culturas):
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return

    for i, c in enumerate(culturas):
        print(
            f"[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} kg"
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
