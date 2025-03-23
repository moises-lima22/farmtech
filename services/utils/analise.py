import subprocess


def executar_analise_r():
    try:
        subprocess.run(["Rscript", "r_scripts/analise.R"], check=True)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o script R:", e)
        return

    while True:
        escolha = input(
            "\nDigite [0] para voltar ao menu principal ou [1] para encerrar o sistema: "
        ).strip()
        if escolha == "0":
            return
        elif escolha == "1":
            print("Saindo do sistema...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
