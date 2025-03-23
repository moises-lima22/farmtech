import subprocess

def obter_previsao_clima():
    try:
        resultado = subprocess.run(
            ["Rscript", "src/r_scripts/clima.R"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return resultado.stdout
    except subprocess.TimeoutExpired:
        return "⏱️  Previsao do tempo demorou para carregar."
    except subprocess.CalledProcessError:
        return "⚠️  Nao foi possivel obter a previsao do tempo."


def exibir_menu():

    while True:
        print("\n========== SISTEMA DE GESTAO AGRICOLA ==========")
        print(obter_previsao_clima().strip())

        print("\n1. Registrar dados de plantio")
        print("2. Consultar analise de area e insumos")
        print("3. Atualizar informacoes de plantio")
        print("4. Excluir registro de plantio")
        print("5. Encerrar sistema")
        print("6. Exportar relatorio em CSV")
        print("7. Executar analise estatistica (R)")
        print("8. Limpar")
        print("================================================")

        try:
            opcao = int(input("\nEscolha uma opcao: "))
            if opcao in range(1, 9):
                return opcao
            else:
                print("❌ Opcao fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número inteiro de 1 a 8.")

