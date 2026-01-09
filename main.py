import os
import json
import matplotlib.pyplot as plt

archivos = os.listdir("proyecto-icd/jsons/mypimes")

def promedio(producto_buscado):
    precios = []
    for archivo in archivos:
        with open(f"proyecto-icd/jsons/mypimes/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["product"]:
                if producto["name"] == producto_buscado:
                    precios.append(producto["precio"])
    
    promedio = round(sum(precios)/len(precios))
    return promedio
        
diccionario = {
    "Pan": promedio("Pan"),
    "Leche": promedio("Leche"),
    "Toallitas húmedas":promedio("Toallitas húmedas"),
    "Pañales":promedio("Pañales"),
    "yogurt":promedio("yogurt"),
    "pollo":promedio("pollo"),
    "picadillo":promedio("picadillo"),
    "huevo":promedio("huevo"),
    "queso":promedio("queso"),
    "sopas":promedio("sopas"),
    "arroz":promedio("arroz"),
    "frijoles":promedio("frijoles"),
    "aceite":promedio("aceite"),
    "cereales":promedio("cereales"),
    "galletas":promedio("galletas")
}

def grafico_precio_promedio_vs_pension_minima(diccionario):
    keys = diccionario.keys()
    values = diccionario.values()

    plt.bar(keys,values,color="#6a4d57")
    plt.axhline(y=3056,color="#9c9386",ls="--",label="Pensión mínima")
    plt.legend()
    plt.title("Precio promedio de productos")
    plt.annotate("Pensión Mínima: 3056",(1,3000),(0,2800))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_servicio_domicilio():
    disponible=0
    nodisponible=0
    for archivo in archivos:
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            if "servicio_a_domicilio" in data:
                            if data["servicio_a_domicilio"]["valor"]==True:
                                disponible += 1
                            else:
                                nodisponible += 1
    plt.pie(
    [disponible, nodisponible],
    labels=["Disponible", "No disponible"],
    autopct='%1.1f%%',
    colors=["#6a4d57", "#9c9386"]
    )
    plt.title("Disponibilidad del servicio a domicilio", fontsize=15, fontweight='bold')
    plt.axis('equal')
    plt.show()


def grafico_precios_marca_producto(producto_buscado="pollo"):
    lista=[]
    for archivo in archivos:
        with open(f"json/{archivo}", encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto["nombre"].lower().strip() == producto_buscado.lower().strip() and producto["disponible"] == True:
                    precio = producto["precio"]
                    unidad_de_medida = str(producto["unidad de medida"])  # revisa si la clave es correcta
                    marca = str(producto["marca"])
                    lista.append({"marca": marca, "precio": precio, "unidad_de_medida": unidad_de_medida})

    dic = {}
    for p in lista:
        marca = p["marca"]
        if marca not in dic or p["precio"] <= dic[marca]["precio"]:
            dic[marca] = p

    lista = sorted(dic.values(), key=lambda x: x["precio"])

    marcas = []
    precios = []
    unidades = []
    for p in lista:
        marcas.append(p["marca"])
        precios.append(p["precio"])
        unidades.append(p["unidad_de_medida"])

    barras = plt.barh(marcas, precios, color="#9c9386")
    plt.bar_label(barras, unidades, label_type="edge")
    plt.title("Precios de " + producto_buscado + " ordenados")
    plt.ylabel("Marca")
    plt.xlabel("Precio")
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.show()


def grafico_disponibilidad_mypimes():
    disponibilidad={}
    for archivo in archivos:
        contador=0
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto["disponible"]==True:
                    contador+=1
                    
        nombre = archivo.replace(".json", "")
        disponibilidad[nombre] = contador
    claves_ordenadas = sorted(disponibilidad.keys(), key=lambda x: int(x.replace("mipyme", "")))
    valores_ordenados = [disponibilidad[k] for k in claves_ordenadas]

    plt.plot(
        claves_ordenadas,valores_ordenados,
        color="#6a4d57",   
        linewidth=3,          
        marker="*",         
        markersize=15 
        )
    plt.title(
        "Disponibilidad de las mipymes",    
    fontsize=16,                    
    fontweight="bold"
    )
    plt.xlabel("Mipymes", fontsize=12)      
    plt.ylabel("Artículos Disponibles ($)", fontsize=12)
    plt.xticks(rotation=45, ha="right")   
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()
def comparacion_precio_mipymes(producto_comparar):
    precios={}
    pension_promedio=4000
    cambio_a_usd=450
    precios_en_usd=[]
    for archivo in archivos:
        with open(f"json/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["productos"]:
                if producto_comparar == producto["nombre"] and producto["disponible"]== True:
                    nombre=archivo.replace(".json","")
                    precios[nombre] = producto["precio"]
    claves_ordenadas = sorted(precios.keys(), key=lambda x: int(x.replace("mipyme", "")))
    
    valores_ordenados = [precios[k] for k in claves_ordenadas]
    
    for x in valores_ordenados:
        nuevo_precio=x/cambio_a_usd
        precios_en_usd.append(nuevo_precio)
        
    plt.scatter(claves_ordenadas,precios_en_usd,s=300,color="#9c9386",marker="*")
    plt.title("Precio del " + producto_comparar + " en usd todas las mipymes")
    plt.axhline(y=pension_promedio/cambio_a_usd,color="black",linestyle="--",linewidth=2,label="Pensión promedio en USD")
    plt.legend()
    plt.text(
         x=-3.50, y=8.90, 
    s=f"Pensión promedio: {8.90:.2f} usd",
    ha="center", va="top", fontsize=10, color="black", backgroundcolor="white")
    plt.xlabel("Mipymes",fontsize=12)
    plt.ylabel("Precio en usd($)",fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

#llamado
grafico_precio_promedio_vs_pension_minima(diccionario)    
comparacion_precio_mipymes(producto_comparar="pollo")
grafico_precios_marca_producto(producto_buscado="pollo")
grafico_disponibilidad_mypimes()            
grafico_servicio_domicilio()            
    