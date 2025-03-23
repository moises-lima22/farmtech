def listar_culturas(culturas, mostrar_rodape: bool = True):
    print("\n========== 🌱 CULTURAS REGISTRADAS ==========\n")

    if not culturas:
        print("Nenhuma cultura cadastrada.")
    else:
        for i, c in enumerate(culturas):
            print(
                f"[{i}] {c['tipo'].capitalize():<6} | "
                f"Área: {c['total_area']:>6.1f} m² | "
                f"Insumo Total: {c['total_insumo']:>6.1f} kg"
            )
            print(f"     📝 {c['descricao']}\n")

    if not mostrar_rodape:
        return

    while True:
        escolha = input(
            "────────────────────────────────────────────────────────\n"
            "Digite [0] para voltar ao menu principal ou [1] para encerrar o sistema: "
        ).strip()
        if escolha == "0":
            return
        elif escolha == "1":
            print("Saindo do sistema...")
            exit()
        else:
            print("❌ Opção inválida. Tente novamente.")
