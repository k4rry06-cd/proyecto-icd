import os
import json
import matplotlib.pyplot as plt

archivos = os.listdir("proyecto-icd/jsons/mypimes")
salario_promedio=7853

def promedio(producto_buscado):
    precios = []
    for archivo in archivos:
        with open(f"proyecto-icd/jsons/mypimes/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["product"]:
                if producto["name"] == producto_buscado:
                    producto["price"]=float(producto["price"])
                    precios.append(producto["price"])
    
    promedio = round(sum(precios)/len(precios))
    return promedio
        
diccionario = {
   "azucar":promedio("Azúcar 1kg"),
    "arroz":promedio("Arroz 1kg"),
    "carton de huevos":promedio("Cartón de Huevo"),
    "pechuga de pollo":promedio("Pechuga de Pollo 2kg"),
    "picadillo":promedio("Picadillo de MDM 1lb"),
    "aceite":promedio("Aceite 1l"),
    "spaghettis":promedio("Spaghettis 500g"),
    "perritos":promedio("Salchichas de Pollo (10u)"),
    "pan":promedio("Pan(8u)")    
}

def por_ciento(parte,total):
    
    porcentajes={}
    for producto, precio in diccionario.items():
        porcentaje=(precio/total)*100
        porcentajes[producto]=porcentaje
    return porcentajes    

def promedio2(precios):
    promedio=round(sum(precios)/len(precios))
    return promedio

def prom_usd(precio):
    with open("proyecto-icd/El toque/el_toque.json","r", encoding="utf-8") as file:
        data = json.load(file)
        precios=[]
        for registro in data.get("datos",[]):
            if "valor" in registro:
                valor=float(registro["valor"])
                precios.append(valor)
    return promedio2(precios)            
                


def grafico_precio_promedio_vs_salario_promedio_en_La_Habana(diccionario):
    keys = diccionario.keys()
    values = diccionario.values()

    plt.bar(keys,values,color="#0ffff8")
    plt.axhline(y=7853,color="#03c9f2",ls="--",label="Salario Promedio")
    plt.legend()
    plt.title("Precio de productos")
    plt.annotate("Salario Promedio en La Habana: 7853",(1,7800),(0,7600))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def que_por_ciento_representa_cada_producto_del_salario(diccionario):
   keys=diccionario.keys()
   values=por_ciento(diccionario.values(),salario_promedio)
   values1=list(values.values())

   plt.figure(figsize=(12,4))
   plt.barh(keys,values1,color="#0985ad")
   plt.gca().invert_yaxis()
   plt.xlabel("Porcentaje del Salario(%)")
   plt.title(f"Cuanto cuestan en base al salario({salario_promedio}cup)")
   plt.tight_layout
   plt.show()

def canasta_basica_al_mes(diccinario):
    productos=["Arroz","Picadillo","Pan","Aceite"]
    precios=[promedio("Arroz 1kg")*5,promedio("Picadillo de MDM 1lb")*5,promedio("Pan(8u)")*4,promedio("Aceite 1l")]   
    total=sum(precios)
    porcentajes=por_ciento(precios,salario_promedio)
    colores=["#d96bff","#00d0ff","#48f77d","#ffeb8d"]
    explode=(0.1,0,0,0)
    fig,ax=plt.subplots(figsize=(10,8))
    wedges, texts, aurotexts =ax.pie(
        precios,
        labels=productos,
        autopct="%1.1f%%",
        startangle=90,
        colors=colores,
        explode=explode,
        shadow=True,
        wedgeprops={"edgecolor":"white","linewidth":2})
    plt.setp(texts,size=12,weight="bold")
    plt.title("Distribución de Gastos Mensuales")
    ax.axis("equal")
    plt.tight_layout()
    plt.show()

def precios_tienda_usd(producto_buscado):
   
    with open("proyecto-icd/jsons/tienda usd estatal/tienda_usd_estatal.json","r", encoding="utf-8") as file:
        data = json.load(file)
        for producto in data["product"]:
                if producto["name"] == producto_buscado:
                    producto["price"]=float(producto["price"])
                    precio=producto["price"]*prom_usd(diccionario)
    return precio     
     
def comparacion_mypimes_usd(diccinario):
    productos=["Azúcar 1kg","Arroz 1kg","Pechuga de Pollo 2kg","Picadillo de MDM 1lb","Aceite 1l"]
    precios_mypimes=[promedio("Azúcar 1kg"),
                     promedio("Arroz 1kg"),
                     promedio("Pechuga de Pollo 2kg"),
                     promedio("Picadillo de MDM 1lb"),
                     promedio("Aceite 1l")] 
    precios_usd=[precios_tienda_usd("Azúcar 1kg"),
                 precios_tienda_usd("Arroz 1kg"),
                 precios_tienda_usd("Pechuga de Pollo 2kg"),
                 precios_tienda_usd("Picadillo de MDM 1lb"),
                 precios_tienda_usd("Aceite 1l")]
    plt.figure(figsize=(12,7))
    posiciones= range(len(productos))
    ancho_barra=0.35
    barras1=plt.bar([p-ancho_barra/2 for p in posiciones], precios_mypimes,
                    width=ancho_barra,label="Mypimes",color="#00455a")
    barras2=plt.bar([p+ancho_barra/2 for p in posiciones],precios_usd,
                    width=ancho_barra,label="Tiendas en USD",color="#915700")
    plt.title("Comparación de Precios por producto", fontsize=16,fontweight="bold")
    plt.xlabel("Productos",fontsize=12)
    plt.ylabel("Precio(USD)",fontsize=12)
    plt.xticks(posiciones,productos)
    plt.legend()
    plt.grid(axis="y",alpha=0.3,linestyle="--")
    plt.tight_layout()
    plt.show()

def minimo(producto_buscado):
    precios = []
    for archivo in archivos:
        with open(f"proyecto-icd/jsons/mypimes/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            for producto in data["product"]:
                if producto["name"] == producto_buscado:
                    producto["price"]=float(producto["price"])
                    precios.append(producto["price"])
    
    minimo = min(precios)
    return minimo


 
#grafico_precio_promedio_vs_salario_promedio_en_La_Habana(diccionario)  
#que_por_ciento_representa_cada_producto_del_salario(diccionario)
#canasta_basica_al_mes(diccionario)
#comparacion_mypimes_usd(diccionario)
