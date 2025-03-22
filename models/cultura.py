def criar_cultura(tipo, dimensoes, ruas=0):
    if tipo.lower() == "café":
        area = dimensoes["largura"] * dimensoes["comprimento"]
        total_insumo = ruas * dimensoes["comprimento"] * 0.5 * 1000  # mL
        return {
            "tipo": "Café",
            "formato_area": "Retângulo",
            "largura": dimensoes["largura"],
            "comprimento": dimensoes["comprimento"],
            "ruas": ruas,
            "insumo": "Fosfato",
            "quantidade_insumo": 0.5,
            "total_area": area,
            "total_insumo": total_insumo
        }
    elif tipo.lower() == "milho":
        area = (dimensoes["base"] * dimensoes["altura"]) / 2
        total_insumo = area * 1  # kg
        return {
            "tipo": "Milho",
            "formato_area": "Triângulo",
            "base": dimensoes["base"],
            "altura": dimensoes["altura"],
            "insumo": "Nitrogênio",
            "quantidade_insumo": 1,
            "total_area": area,
            "total_insumo": total_insumo
        }
