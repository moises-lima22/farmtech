from models.cultura import criar_cultura


def solicitar_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada == "x":
            return "x"
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            else:
                print("❌ O valor deve ser maior que zero.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido ou 'x' para voltar.")


def inserir_cultura(culturas):
    while True:
        tipo = input(
            "\nDigite o tipo de cultura (cana ou milho) ou 'x' para voltar: "
        ).lower()
        if tipo == "x":
            print("\n🔙 Retornando ao menu principal.")
            return
        if tipo not in ["cana", "milho"]:
            print(
                "❌ Tipo de cultura inválido! Tente novamente ou digite 'x' para voltar."
            )
            continue

        if tipo == "cana":
            largura = solicitar_valor("Largura da área (m): ")
            if largura == "x":
                return
            comprimento = solicitar_valor("Comprimento da área (m): ")
            if comprimento == "x":
                return
            dados = {"largura": largura, "comprimento": comprimento}

        else:  # milho
            base = solicitar_valor("Base da área (m): ")
            if base == "x":
                return
            altura = solicitar_valor("Altura da área (m): ")
            if altura == "x":
                return
            dados = {"base": base, "altura": altura}

        try:
            cultura = criar_cultura(tipo, dados)
        except Exception as e:
            print(f"❌ Erro ao criar cultura: {e}")
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
