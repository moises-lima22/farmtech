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
