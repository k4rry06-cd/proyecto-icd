import json
import os

def cargar_productos_por_nombre(carpeta, cantidad):
    acumulador = {}

    for i in range(1, cantidad + 1):
        archivo = f"mipyme_{i:02}.json"
        ruta = os.path.join(carpeta, archivo)

        with open(ruta, 'r', encoding='utf-8') as f:
            data = json.load(f)
            productos = data["product"]

            for p in productos:
                nombre = p["name"]
                precio = float(p["price"])
                if nombre not in acumulador:
                    acumulador[nombre] = []
                acumulador[nombre].append(precio)

    return acumulador

def calcular_promedios(acumulador):
    promedios = {}
    for nombre, precios in acumulador.items():
        if precios:
            promedios[nombre] = sum(precios) / len(precios)
    return promedios

def graficar_promedios(promedios):
    nombres = list(promedios.keys())
    valores = list(promedios.values())

    plt.figure(figsize=(12, 6))
    plt.bar(nombres, valores, color="#5e4d3b")
    plt.axhline(y=3056, color="#533527", ls="--", label="Pensión mínima")
    plt.title("Precio promedio por nombre de producto")
    plt.xlabel("Nombre del producto")
    plt.ylabel("Precio promedio (CUP)")
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.legend()
    plt.tight_layout()
    plt.show()