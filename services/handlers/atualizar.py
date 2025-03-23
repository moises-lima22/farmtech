from services.handlers.listar import listar_culturas
from models.cultura import criar_cultura


def atualizar_cultura(culturas):
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return

    listar_culturas(culturas, mostrar_rodape=False)

    while True:
        entrada = input(
            "\nDigite o índice da cultura a ser atualizada ou 'x' para voltar ao menu principal: "
        ).strip()
        if entrada.lower() == "x":
            print("🔙 Retornando ao menu principal.")
            return

        try:
            index = int(entrada)
            if not (0 <= index < len(culturas)):
                print("❌ Índice inválido.")
                continue

            cultura_original = culturas[index]
            tipo = cultura_original["tipo"]
            print(f"\n🔄 Atualizando cultura do tipo: {tipo}")

            if tipo == "cana":
                largura = input(f"Largura atual ({cultura_original['largura']} m): ")
                comprimento = input(
                    f"Comprimento atual ({cultura_original['comprimento']} m): "
                )

                largura = (
                    float(largura) if largura.strip() else cultura_original["largura"]
                )
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

            else:
                base = input(f"Base atual ({cultura_original['base']} m): ")
                altura = input(f"Altura atual ({cultura_original['altura']} m): ")

                base = float(base) if base.strip() else cultura_original["base"]
                altura = float(altura) if altura.strip() else cultura_original["altura"]

                if base <= 0 or altura <= 0:
                    print("❌ Valores devem ser maiores que zero.")
                    return

                cultura = criar_cultura(tipo, {"base": base, "altura": altura})

            # Exibe preview
            print("\n📋 Visualização da cultura atualizada:")
            print(
                f"\n{cultura['tipo']} - Área: {cultura['total_area']} m² - Insumo Total: {cultura['total_insumo']} kg"
            )
            print(f"Descrição: {cultura['descricao']}")

            while True:
                confirmar = input(
                    "\nDeseja salvar esta atualização? (s/n ou 'x' para cancelar): "
                ).lower()
                if confirmar == "x":
                    print("❌ Atualização cancelada.")
                    return
                elif confirmar == "s":
                    culturas[index] = cultura
                    print("✅ Cultura atualizada com sucesso.")
                    return
                elif confirmar == "n":
                    print("❌ Atualização cancelada.")
                    return
                else:
                    print("❌ Entrada inválida. Digite 's', 'n' ou 'x'.")

        except ValueError:
            print("❌ Entrada inválida. Digite um número válido ou 'x' para voltar.")
