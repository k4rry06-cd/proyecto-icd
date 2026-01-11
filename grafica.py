import matplotlib.pyplot as plt
import numpy as np

# Configuración del estilo para mejor visualización
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.figsize'] = [14, 8]
plt.rcParams['figure.dpi'] = 100

# Precios de productos básicos en Cuba (pesos cubanos - CUP)
# Datos representativos de 2024 - valores aproximados del mercado informal/agropecuario
productos = [
    'Arroz (1kg)', 'Frijoles (1kg)', 'Aceite (1L)', 'Pollo (1kg)', 
    'Carne de cerdo (1kg)', 'Huevos (10 un)', 'Pan (1 un)', 
    'Leche en polvo (400g)', 'Queso (1kg)', 'Azúcar (1kg)',
    'Café (250g)', 'Spaghetti (500g)', 'Tomates (1kg)', 
    'Plátanos (1lb)', 'Jabón de baño (1 un)', 'Pasta dental (1 un)'
]

precios = [
    450, 650, 1200, 900, 1100, 650, 50, 1800, 3500, 300,
    2500, 250, 500, 150, 350, 450
]

# Cálculo del precio promedio
precio_promedio = np.mean(precios)

# Crear figura con dos subtramas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# =========== GRÁFICA 1: Barras de precios individuales ===========
bars = ax1.barh(productos, precios, color=plt.cm.viridis(np.linspace(0.4, 0.9, len(productos))), edgecolor='black', linewidth=0.5)
ax1.axvline(x=precio_promedio, color='red', linewidth=3, linestyle='--', alpha=0.8, label=f'Promedio: {precio_promedio:.0f} CUP')

# Añadir etiquetas de valores a cada barra
for bar, precio in zip(bars, precios):
    ax1.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2, 
             f'{precio:,} CUP', va='center', fontsize=10, fontweight='bold')

# Personalizar gráfica 1
ax1.set_xlabel('Precio en Pesos Cubanos (CUP)', fontsize=12, fontweight='bold')
ax1.set_title('PRECIOS DE PRODUCTOS BÁSICOS - CUBA (2024)\nMercado Informal/Agropecuario', 
              fontsize=16, fontweight='bold', pad=20, color='darkred')
ax1.invert_yaxis()  # Invertir para que el producto más caro quede arriba
ax1.grid(True, alpha=0.3, axis='x')
ax1.legend(loc='lower right', fontsize=12)
ax1.set_xlim(0, max(precios) * 1.15)  # Añadir 15% de margen

# =========== GRÁFICA 2: Distribución y estadísticas ===========
# Crear datos para la gráfica de distribución
categorias_precio = ['< 500 CUP', '500-1000 CUP', '1000-2000 CUP', '> 2000 CUP']
conteos = [0, 0, 0, 0]

for precio in precios:
    if precio < 500:
        conteos[0] += 1
    elif precio <= 1000:
        conteos[1] += 1
    elif precio <= 2000:
        conteos[2] += 1
    else:
        conteos[3] += 1

# Gráfico de pastel para distribución de precios
colors_pie = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']
wedges, texts, autotexts = ax2.pie(conteos, labels=categorias_precio, autopct='%1.1f%%',
                                   colors=colors_pie, startangle=90, explode=(0.05, 0.05, 0.05, 0.1),
                                   shadow=True, textprops={'fontsize': 11})

# Mejorar los textos de porcentaje
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Añadir caja con estadísticas
estadisticas_texto = (
    f'ESTADÍSTICAS DE PRECIOS\n'
    f'─────────────────────\n'
    f'• Precio promedio: {precio_promedio:.0f} CUP\n'
    f'• Producto más caro: {productos[precios.index(max(precios))]}\n'
    f'• Precio máximo: {max(precios):,} CUP\n'
    f'• Producto más barato: {productos[precios.index(min(precios))]}\n'
    f'• Precio mínimo: {min(precios):,} CUP\n'
    f'• Rango total: {max(precios)-min(precios):,} CUP\n'
    f'• Cantidad productos: {len(productos)}'
)

# Posicionar texto de estadísticas
ax2.text(0.95, 0.05, estadisticas_texto, transform=ax2.transAxes,
         fontsize=11, verticalalignment='bottom',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8, edgecolor='brown'))

ax2.set_title('DISTRIBUCIÓN POR RANGOS DE PRECIO', fontsize=14, fontweight='bold', pad=20)

# =========== ANOTACIÓN GLOBAL ===========
# Calcular relación con salario mínimo
salario_minimo = 2100  # CUP (aproximado)
productos_promedio_salario_minimo = salario_minimo / precio_promedio

# Añadir información contextual en la figura
fig.suptitle('ANÁLISIS DEL COSTO DE LA VIDA EN CUBA: ¿CUÁNTO CUESTA LO BÁSICO?', 
             fontsize=18, fontweight='bold', y=1.02, color='darkblue')

contexto_texto = (
    f'CONTEXTO ECONÓMICO:\n'
    f'• Salario mínimo mensual: {salario_minimo:,} CUP\n'
    f'• Con 1 salario mínimo se pueden comprar {productos_promedio_salario_minimo:.1f} productos del promedio\n'
    f'• Para comprar 1 unidad de cada producto se necesitan: {sum(precios):,} CUP\n'
    f'→ Esto equivale a {(sum(precios)/salario_minimo):.1f} veces el salario mínimo'
)

fig.text(0.5, 0.01, contexto_texto, ha='center', fontsize=12, 
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.9, edgecolor='navy', linewidth=2))

plt.tight_layout(rect=[0, 0.08, 1, 0.98])  # Ajustar layout para incluir el texto inferior
plt.show()

# =========== GRÁFICA ADICIONAL: Relación con salarios ===========
# (Si quieres mostrar también esta relación)
fig2, ax3 = plt.subplots(figsize=(12, 6))

# Datos de salarios para comparación
salarios = ['Mínimo', 'Promedio', 'Profesional']
valores_salarios = [2100, 4500, 8000]  # Valores aproximados en CUP

# Calcular cuántos productos del promedio se pueden comprar con cada salario
productos_comprables = [s / precio_promedio for s in valores_salarios]

x = range(len(salarios))
bars_salarios = ax3.bar(x, productos_comprables, color=['#e74c3c', '#3498db', '#2ecc71'], edgecolor='black')

ax3.set_xlabel('Tipo de Salario', fontsize=12, fontweight='bold')
ax3.set_ylabel('Productos promedio que se pueden comprar', fontsize=12, fontweight='bold')
ax3.set_title('PODER ADQUISITIVO: ¿CUÁNTOS PRODUCTOS DEL PROMEDIO SE PUEDEN COMPRAR?', 
              fontsize=14, fontweight='bold', pad=20)
ax3.set_xticks(x)
ax3.set_xticklabels(salarios, fontsize=11, fontweight='bold')

# Añadir etiquetas con valores exactos
for bar, valor in zip(bars_salarios, productos_comprables):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{valor:.1f} productos', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Añadir línea de referencia para "canasta básica" (considerando 15 productos esenciales)
ax3.axhline(y=15, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Canasta básica mínima (15 productos)')
ax3.legend(loc='upper left')

# Información adicional
info_adicional = f"Considerando el precio promedio de {precio_promedio:.0f} CUP por producto"
fig2.text(0.5, 0.01, info_adicional, ha='center', fontsize=11, style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()