from services.handlers.listar import listar_culturas
from models.cultura import criar_cultura
from services.utils.solicitar_valor import (
    solicitar_valor,
)


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

            original = culturas[index]
            tipo = original["tipo"]
            print(f"\n🔄 Atualizando cultura do tipo: {tipo}")

            if tipo == "cana":
                larguraNova = solicitar_valor(
                    f"Largura atual ({original['largura']} m): "
                )

                if larguraNova == "x":
                    return

                comprimentoNovo = solicitar_valor(
                    f"Comprimento atual ({original['comprimento']} m): "
                )

                if comprimentoNovo == "x":
                    return

                nova_cultura = criar_cultura(
                    tipo, {"largura": larguraNova, "comprimento": comprimentoNovo}
                )

            else:
                baseNova = solicitar_valor(f"Base atual ({original['base']} m): ")

                if baseNova == "x":
                    return

                alturaNova = solicitar_valor(f"Altura atual ({original['altura']} m): ")

                if alturaNova == "x":
                    return

                nova_cultura = criar_cultura(
                    tipo, {"base": baseNova, "altura": alturaNova}
                )

            # Exibir preview
            print("\n📋 Visualização da cultura atualizada:\n")
            print(
                f"{nova_cultura['tipo'].capitalize():<6} | Área: {nova_cultura['total_area']:>6.1f} m² | Insumo Total: {nova_cultura['total_insumo']:>6.1f} kg"
            )
            print(f"     📝 {nova_cultura['descricao']}")

            while True:
                confirmar = input(
                    "\nDeseja salvar esta atualização? (s/n ou 'x' para cancelar): "
                ).lower()
                if confirmar == "x":
                    print("❌ Atualização cancelada.")
                    return
                elif confirmar == "s":
                    culturas[index] = nova_cultura
                    print("✅ Cultura atualizada com sucesso.")
                    return
                elif confirmar == "n":
                    print("❌ Atualização cancelada.")
                    return
                else:
                    print("❌ Entrada inválida. Digite 's', 'n' ou 'x'.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido ou 'x' para voltar.")
