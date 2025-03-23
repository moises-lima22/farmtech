def remover_cultura(culturas):
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return

    for i, c in enumerate(culturas):
        print(
            f"[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} kg"
        )
        print(f"Descrição: {c['descricao']}")

    while True:
        entrada = input(
            "\nDigite o índice da cultura a ser removida ou 'x' para voltar ao menu principal: "
        ).strip()
        if entrada.lower() == "x":
            print("🔙 Retornando ao menu principal.")
            return

        try:
            index = int(entrada)
            if not (0 <= index < len(culturas)):
                print("❌ Índice inválido.")
                continue

            while True:
                confirmacao = input(
                    "Tem certeza que deseja remover esta cultura? (s/n ou 'x' para cancelar): "
                ).lower()
                if confirmacao == "x":
                    print("❌ Remoção cancelada.")
                    return
                elif confirmacao == "s":
                    culturas.pop(index)
                    print("✅ Cultura removida com sucesso.")
                    return
                elif confirmacao == "n":
                    print("❌ Operação cancelada.")
                    return
                else:
                    print("❌ Entrada inválida. Digite 's', 'n' ou 'x'.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido ou 'x' para voltar.")
