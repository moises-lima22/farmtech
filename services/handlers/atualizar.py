from models.cultura import criar_cultura


def atualizar_cultura(culturas):
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return

    def exibir_culturas():
        for i, cultura in enumerate(culturas):
            print(
                f"[{i}] {cultura['tipo']} - Área: {cultura['total_area']} m² - Insumo Total: {cultura['total_insumo']} kg"
            )
            print(f"Descrição: {cultura['descricao']}")

    def solicitar_indice():
        while True:
            entrada = input(
                "\nDigite o índice da cultura a ser atualizada ou 'x' para voltar ao menu principal: "
            ).strip()
            if entrada.lower() == "x":
                print("🔙 Retornando ao menu principal.")
                return None
            if entrada.isdigit():
                indice = int(entrada)
                if 0 <= indice < len(culturas):
                    return indice
                else:
                    print("❌ Índice fora do intervalo.")
            else:
                print(
                    "❌ Entrada inválida. Digite um número válido ou 'x' para voltar."
                )

    def solicitar_valor_numerico(mensagem, atual):
        while True:
            entrada = input(
                f"{mensagem} ({atual} m) ou pressione Enter para manter: "
            ).strip()
            if entrada == "":
                return atual
            try:
                valor = float(entrada)
                if valor > 0:
                    return valor
                else:
                    print("❌ O valor deve ser maior que zero.")
            except ValueError:
                print("❌ Entrada inválida. Digite um número válido.")

    def atualizar_campos(tipo, original):
        if tipo == "cana":
            largura = solicitar_valor_numerico("Largura atual", original["largura"])
            comprimento = solicitar_valor_numerico(
                "Comprimento atual", original["comprimento"]
            )
            return criar_cultura(tipo, {"largura": largura, "comprimento": comprimento})
        else:
            base = solicitar_valor_numerico("Base atual", original["base"])
            altura = solicitar_valor_numerico("Altura atual", original["altura"])
            return criar_cultura(tipo, {"base": base, "altura": altura})

    def confirmar_atualizacao(nova_cultura):
        print("\n📋 Visualização da cultura atualizada:")
        print(
            f"\n{nova_cultura['tipo']} - Área: {nova_cultura['total_area']} m² - Insumo Total: {nova_cultura['total_insumo']} kg"
        )
        print(f"Descrição: {nova_cultura['descricao']}")
        while True:
            confirmar = (
                input("\nDeseja salvar esta atualização? (s/n): ").strip().lower()
            )
            if confirmar == "s":
                return True
            elif confirmar == "n":
                return False
            else:
                print("❌ Resposta inválida. Digite 's' para sim ou 'n' para não.")

    # fluxo principal
    exibir_culturas()
    indice = solicitar_indice()
    if indice is None:
        return

    original = culturas[indice]
    tipo = original["tipo"]
    print(f"\n🔄 Atualizando cultura do tipo: {tipo}")

    nova_cultura = atualizar_campos(tipo, original)

    if confirmar_atualizacao(nova_cultura):
        culturas[indice] = nova_cultura
        print("✅ Cultura atualizada com sucesso.")
    else:
        print("❌ Atualização cancelada.")
