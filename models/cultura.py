def criar_cultura(tipo, dimensoes):
    if tipo.lower() == "cana":
        area = dimensoes["largura"] * dimensoes["comprimento"]
        total_insumo = area * 2
        return {
            "tipo": "cana",
            "descricao": (
                "Plantio de cana-de-açúcar em área retangular com aplicação de potássio "
                "à razão de 2 kg por metro quadrado, visando o fortalecimento radicular "
                "e o desenvolvimento inicial da cultura."
            ),
            "formato_area": "retangulo",
            "largura": dimensoes["largura"],
            "comprimento": dimensoes["comprimento"],
            "insumo": "potassio",
            "quantidade_insumo": 2,
            "total_area": area,
            "total_insumo": total_insumo,
        }
    elif tipo.lower() == "milho":
        area = (dimensoes["base"] * dimensoes["altura"]) / 2
        total_insumo = area * 1
        return {
            "tipo": "milho",
            "descricao": (
                "Plantio de milho em área triangular com aplicação de nitrogênio "
                "na proporção de 1 kg por metro quadrado, promovendo o crescimento "
                "vegetativo e a produtividade da lavoura."
            ),
            "formato_area": "triangulo",
            "base": dimensoes["base"],
            "altura": dimensoes["altura"],
            "insumo": "nitrogenio",
            "quantidade_insumo": 1,
            "total_area": area,
            "total_insumo": total_insumo,
        }
