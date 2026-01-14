#Importo el json, matplotlib y lo necesario
import os
import json
import matplotlib.pyplot as plt

#Guardo todos los json 
archivos = os.listdir("jsons/mypimes")

#Establezco el salario promedio para que sea más cómodo
salario_promedio=7853

#Esta es una función para calcular el promedio de los productos solicitados
def promedio(producto_buscado):
    precios = []
    #Cargo todos los json
    for archivo in archivos:
        with open(f"jsons/mypimes/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            #Busco el dato que me hace falta
            for producto in data["product"]:
                if producto["name"] == producto_buscado:
                    producto["price"]=float(producto["price"])
                    precios.append(producto["price"])
    #Saco el promedio
    promedio = round(sum(precios)/len(precios))
    return promedio

 #Creo un diccionario que contenga el preciopromedio de todos los productos       
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

#Creo una función para calcular el por ciento
def por_ciento(parte,total):
    
    porcentajes={}
    for producto, precio in diccionario.items():
        porcentaje=(precio/total)*100
        porcentajes[producto]=porcentaje
    return porcentajes   
 
#Creo una función para calcular el promedio pero sin cargar los json
def promedio2(precios):
    promedio=round(sum(precios)/len(precios))
    return promedio

#Creo una función que calcule el promedio de los datos de el json de eltoque
def prom_usd(precio):
    with open("El toque/el_toque.json","r", encoding="utf-8") as file:
        data = json.load(file)
        precios=[]
        #Extraigo el valor i calculo el promedio
        for registro in data.get("datos",[]):
            if "valor" in registro:
                valor=float(registro["valor"])
                precios.append(valor)
    return promedio2(precios)            
                

#Creo la primera gráfica
def grafico_precio_promedio_vs_salario_promedio_en_La_Habana(diccionario):
    #Obtengo los valores y llaves del diccionario
    keys = diccionario.keys()
    values = diccionario.values()

    #Creo la gráfica de barras con matplotlib
    plt.bar(keys,values,color="#0ffff8")
    plt.axhline(y=7853,color="#03c9f2",ls="--",label="Salario Promedio")
    plt.legend()
    plt.title("Precio de productos")
    plt.annotate("Salario Promedio en La Habana: 7853",(1,7800),(0,7600))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#Creo la gráfica 2
def que_por_ciento_representa_cada_producto_del_salario(diccionario):
   #Cargo los valores y llaves del diccionario, saco la relación del porciento y convierto los valores en una lista
   keys=diccionario.keys()
   values=por_ciento(diccionario.values(),salario_promedio)
   values1=list(values.values())

#Creo la gráfica con matplotlib
   plt.figure(figsize=(12,4))
   plt.barh(keys,values1,color="#0985ad")
   plt.gca().invert_yaxis()
   plt.xlabel("Porcentaje del Salario(%)")
   plt.title(f"Costo de los productos en base al salario({salario_promedio}cup)")
   plt.tight_layout
   plt.show()

#Creo la gráfica 3
def canasta_basica_al_mes(diccinario):
    #Como esta gráfica es distinta y más resumida uso menos productos
    productos=["arroz","picadillo","pan","aceite"]
    #Calculo una lista con los precios utilizando promedio, además lo multiplico ya que estamos viendo la cantidad de productos usados en un mes
    precios=[promedio("Arroz 1kg")*5,promedio("Picadillo de MDM 1lb")*5,promedio("Pan(8u)")*4,promedio("Aceite 1l")]   
    total=sum(precios)
    #Transformo los precios en porcentajes y luego enlistas
    precios_dict = {producto: precio for producto,precio in zip(productos,precios)}
    porcentajes_dict=por_ciento(precios_dict,salario_promedio)
    porcentajes = [porcentajes_dict[producto] for producto in productos]
    #Creo la gráfica con matplotlib
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
    #Creo la leyenda de la gráfica
    leyenda_labels=[]
    for producto,precio, in zip(productos,precios):
        porcentaje=porcentajes_dict[producto]
        leyenda_labels.append(f"{producto}: {precio:.2f}cup ")
            
   
    plt.legend(wedges,leyenda_labels,
               title="Detalle de Gastos",
               loc="center left",
               bbox_to_anchor=(1,0,0.5,1),
               fontsize=10 )
    plt.title("Distribución de Gastos Mensuales")
    ax.axis("equal")
    plt.tight_layout()
    plt.show()

#Creo una función que coja el precio en usd y lo convierta a cup
def precios_tienda_usd(producto_buscado):
   #Cargo el json
    with open("jsons/tienda usd estatal/tienda_usd_estatal.json","r", encoding="utf-8") as file:
        data = json.load(file)
        #Cargo el archivo y hago el cambio usando la función de calcular el promedio de el toque
        for producto in data["product"]:
                if producto["name"] == producto_buscado:
                    producto["price"]=float(producto["price"])
                    precio=producto["price"]*prom_usd(diccionario)
    return precio
     
#Creo la gráfica 4 que es para comparar las mypimes con las tiendas usd     
def comparacion_mypimes_usd(diccinario):
    #Creo 3 listas una para el nombre de los productos y otras dos para los precios
    productos=["Azúcar","Arroz","Pechuga de Pollo","Picadillo de MDM","Aceite"]
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
    #Creo la gráfica con matplotlib
    plt.figure(figsize=(12,7))
    posiciones= range(len(productos))
    ancho_barra=0.35
    #Aqui tengo que crear dos barras distintas en diferentes posiciones para comparar
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

#Creo una función para calcular el mínimo de cada producto es parecida a la del promedio
def minimo(producto_buscado):
    precios = []
    #Cargo los archivos
    for archivo in archivos:
        with open(f"jsons/mypimes/{archivo}",encoding="utf-8") as file:
            data = json.load(file)
            #Busco los precios
            for producto in data["product"]:
                if producto["name"] == producto_buscado:
                    producto["price"]=float(producto["price"])
                    precios.append(producto["price"])
    #Saco el minimo
    minimo = min(precios)
    return minimo

#Creo la gráfica 5 que es para ver la evolución del dólar
def variacion_del_usd(diccinario):
    #Cargar el json
    with open("El toque/el_toque.json","r") as f:
        data = json.load(f)
    #Obtener los valores para la gráfica    
    fechas = [item["fecha"] for item in data["datos"]]
    valores = [item["valor"] for item in data["datos"]]
    #Creo la gráfica con matplotlib   
    plt.figure(figsize=(12,6)) 
    plt.plot(fechas, valores, color="#455ba2",alpha=0.7,marker="o",markersize=6,linewidth=2)
    plt.title("Variación del USD por Fecha", fontsize=14, fontweight="bold")
    plt.xlabel("Fecha",fontsize=12)
    plt.ylabel("Valor(USD)",fontsize=12)
    #Hago un código para dividir las fechas por períodos
    if len(fechas)>20:
        paso=max(1,len(fechas)//10)
        indices_mostrar = list(range(0,len(fechas),paso))
        fechas_mostrar= [fechas[i] for i in indices_mostrar]
        plt.xticks(indices_mostrar,fechas_mostrar,rotation=45,fontsize=9)
    else:
        plt.xticks(rotation=45, fontsize=8,ha="right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

#Creo otro diccionario parecido al del promedio pero con el minimo    
diccionario1={"azucar":minimo("Azúcar 1kg"),
    "arroz":minimo("Arroz 1kg"),
    "carton de huevos":minimo("Cartón de Huevo"),
    "pechuga de pollo":minimo("Pechuga de Pollo 2kg"),
    "picadillo":minimo("Picadillo de MDM 1lb"),
    "aceite":minimo("Aceite 1l"),
    "spaghettis":minimo("Spaghettis 500g"),
    "perritos":minimo("Salchichas de Pollo (10u)"),
    "pan":minimo("Pan(8u)")    }    

#Creo la gráfica 6 para comparar también asi que es similar a la otra
def comparacion_prom_vs_min(diccinario):
    #Convierto los datos en listas
    productos=list(diccionario.keys())
    precios_prom=list(diccionario.values()) 
    precios_min=list(diccionario1.values())
    #Sigo con la gráfica
    plt.figure(figsize=(12,7))
    posiciones= range(len(productos))
    ancho_barra=0.35
    barras1=plt.bar([p-ancho_barra/2 for p in posiciones], precios_prom,
                    width=ancho_barra,label="Precios promedio",color="#0f5a00")
    barras2=plt.bar([p+ancho_barra/2 for p in posiciones],precios_min,
                    width=ancho_barra,label="Precios minimos",color="#910018")
    plt.title("Comparación de Precios por producto", fontsize=16,fontweight="bold")
    plt.xlabel("Productos",fontsize=12)
    plt.ylabel("Precio(USD)",fontsize=12)
    plt.xticks(posiciones,productos,rotation=45)
    plt.legend()
    plt.grid(axis="y",alpha=0.3,linestyle="--")
    plt.tight_layout()
    plt.show()   

#Creo la gráfica 7 para mas por ceintos con pastel
def por_ciento_precios_min(diccinario):
    #Creo las listas una para los nombres y otra para los precios
    productos=["arroz","picadillo","pan","aceite"]
    precios=[minimo("Arroz 1kg")*5,minimo("Picadillo de MDM 1lb")*5,minimo("Pan(8u)")*4,minimo("Aceite 1l")]   
    total=sum(precios)
    #Convierto los datos a por cientos y los paso a listas
    precios_dict = {producto: precio for producto,precio in zip(productos,precios)}
    porcentajes_dict=por_ciento(precios_dict,salario_promedio)
    porcentajes = [porcentajes_dict[producto] for producto in productos]
    #Sigo con la gráfica
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
    #Creo las leyendas
    leyenda_labels=[]
    for producto,precio, in zip(productos,precios):
        porcentaje=porcentajes_dict[producto]
        leyenda_labels.append(f"{producto}: {precio:.2f}cup ")
            
   
    plt.legend(wedges,leyenda_labels,
               title="Detalle de Gastos",
               loc="center left",
               bbox_to_anchor=(1,0,0.5,1),
               fontsize=10 )
    plt.title("Distribución de Gastos Mensuales")
    ax.axis("equal")
    plt.tight_layout()
    plt.show()
 

