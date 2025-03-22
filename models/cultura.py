def criar_cultura(tipo, dimensoes):
    if tipo.lower() == "cana":
        area = dimensoes["largura"] * dimensoes["comprimento"]
        total_insumo = area * 2
        return {
            "tipo": "cana",
            "descricao": "Cultura de cana-de-acucar com aplicacao de potassio por metro quadrado.",
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
            "descricao": "Cultura de milho em area triangular com aplicacao de nitrogenio.",
            "formato_area": "triangulo",
            "base": dimensoes["base"],
            "altura": dimensoes["altura"],
            "insumo": "nitrogenio",
            "quantidade_insumo": 1,
            "total_area": area,
            "total_insumo": total_insumo,
        }
