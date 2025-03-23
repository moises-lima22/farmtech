import os
from utils.menu import exibir_menu
from utils.limpar_console import limpar_console
from models.cultura import criar_cultura
from services.handlers.inserir import inserir_cultura
from services.handlers.listar import listar_culturas
from services.handlers.atualizar import atualizar_cultura
from services.handlers.remover import remover_cultura
from services.utils.exportar import exportar_para_csv
from services.utils.analise import executar_analise_r

# Inicializa a lista de culturas com exemplos
culturas = [
    criar_cultura("cana", {"largura": 10, "comprimento": 50}),
    criar_cultura("milho", {"base": 30, "altura": 60}),
]

# Garante que a pasta 'data/' exista
os.makedirs("data", exist_ok=True)

# Loop principal do sistema
while True:
    opcao = exibir_menu()

    match opcao:
        case 1:
            inserir_cultura(culturas)
        case 2:
            listar_culturas(culturas)
        case 3:
            atualizar_cultura(culturas)
        case 4:
            remover_cultura(culturas)
        case 5:
            print("\nEncerrando o programa. Até logo!")
            break
        case 6:
            exportar_para_csv(culturas)
        case 7:
            exportar_para_csv(culturas)
            executar_analise_r()
        case 8:
            limpar_console()
        case _:
            print("\n❌ Opção inválida. Tente novamente.")
