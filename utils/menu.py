import os
import subprocess

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def obter_previsao_clima():
    try:
        resultado = subprocess.run(
            ["Rscript", "r_scripts/clima.R"],
            capture_output=True,
            text=True,
            # timeout=5
        )
        return resultado.stdout
    except subprocess.TimeoutExpired:
        return "⏱️  Previsao do tempo demorou para carregar."
    except subprocess.CalledProcessError:
        return "⚠️  Nao foi possivel obter a previsao do tempo."


def exibir_menu():
    limpar_console()

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

        try:
            opcao = int(input("\nEscolha uma opcao: "))
            if opcao in range(1, 8):
                return opcao
            else:
                print("❌ Opcao fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número inteiro de 1 a 7.")

