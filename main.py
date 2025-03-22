from utils.menu import exibir_menu
from services.manipulador import inserir_cultura, listar_culturas, atualizar_cultura, remover_cultura

culturas = []

while True:
    opcao = exibir_menu()

    if opcao == 1:
        inserir_cultura(culturas)
    elif opcao == 2:
        listar_culturas(culturas)
    elif opcao == 3:
        atualizar_cultura(culturas)
    elif opcao == 4:
        remover_cultura(culturas)
    elif opcao == 5:
        print("\nEncerrando o programa. Até logo!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
