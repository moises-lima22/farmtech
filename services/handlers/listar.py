def listar_culturas(culturas):
    print("\n========== 🌱 CULTURAS REGISTRADAS ==========\n")

    if not culturas:
        print("Nenhuma cultura cadastrada.")
    else:
        for i, c in enumerate(culturas):
            print(
                f"[{i}] {c['tipo']} - Área: {c['total_area']} m² - Insumo Total: {c['total_insumo']} kg"
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
