import numpy as np
import matplotlib.pyplot as plt

# ================================
# Funciones auxiliares
# ================================
def f(x, m):
    """Función parabólica: f(x) = x² - mx + m + 15"""
    return x**2 - m*x + m + 15

def calcular_vertice(m):
    """Calcula coordenadas del vértice"""
    Vx = m / 2
    Vy = f(Vx, m)
    return Vx, Vy

def calcular_E(m):
    """Calcula E = m² - m + 1"""
    return m**2 - m + 1

def graficar_parabola(m, titulo_extra=""):
    """Genera gráfica para un valor de m"""
    x = np.linspace(m/2 - 6, m/2 + 6, 500)
    y = f(x, m)
    Vx, Vy = calcular_vertice(m)
    
    plt.figure(figsize=(10, 6))
    
    # Parábola
    plt.plot(x, y, color='#2E86AB', linewidth=2.5, 
             label=f'$f(x) = x^2 - {m:.0f}x + {m + 15:.0f}$')
    
    # Ejes
    plt.axhline(y=0, color='#333333', linewidth=1.2, alpha=0.7, label='Eje X')
    plt.axvline(x=0, color='#333333', linewidth=1.2, alpha=0.7)
    plt.axvline(x=Vx, color='#A23B72', linestyle='--', linewidth=1.2, 
                alpha=0.6, label=f'$x = {Vx:.1f}$')
    
    # Puntos importantes
    plt.scatter([Vx], [Vy], color='#F18F01', s=150, zorder=5, 
                edgecolors='white', linewidths=2,
                label=f'Vértice $({Vx:.1f}, {Vy:.1f})$')
    plt.scatter([Vx], [0], color='#C73E1D', s=120, zorder=5, 
                marker='s', edgecolors='white', linewidths=1.5,
                label='Punto de tangencia')
    
    # Configuración
    plt.xlabel('x', fontsize=12, fontweight='bold')
    plt.ylabel('f(x)', fontsize=12, fontweight='bold')
    plt.title(f'Parábola tangente al eje X con m = {m:.0f}{titulo_extra}', 
              fontsize=14, fontweight='bold', pad=15)
    plt.grid(True, linestyle='--', alpha=0.4, linewidth=0.8)
    plt.gca().set_facecolor('#F8F9FA')
    plt.legend(loc='upper right', framealpha=0.95, edgecolor='gray', fontsize=10)
    
    # Ajuste automático de límites
    y_min, y_max = min(y), max(y)
    margin = (y_max - y_min) * 0.1
    plt.ylim([y_min - margin, y_max + margin])
    
    plt.tight_layout()
    plt.show()

# ================================
# ANÁLISIS PRINCIPAL
# ================================

# 1. Encontrar valores de m para tangencia
print("="*60)
print("ANÁLISIS DE PARÁBOLAS TANGENTES AL EJE X")
print("="*60)

m_solutions = np.roots([1, -4, -60])
print(f"\nSoluciones para m (discriminante = 0): {m_solutions}")

# 2. Analizar cada solución
print("\n" + "─"*60)
for m in m_solutions:
    Vx, Vy = calcular_vertice(m)
    E = calcular_E(m)
    print(f"\nPara m = {m:.1f}:")
    print(f"  • Vértice: ({Vx:.1f}, {Vy:.1f})")
    print(f"  • E = m² - m + 1 = {E:.0f}")

# 3. Resultado final
print("\n" + "="*60)
print("RESULTADOS FINALES")
print("="*60)
for m in m_solutions:
    print(f"m = {m:.0f}: E = {calcular_E(m):.0f}")
print("="*60)

# 4. Graficar para cada m
for m in m_solutions:
    graficar_parabola(m)

# BONUS: Comparar ambas parábolas
plt.figure(figsize=(12, 7))
x_global = np.linspace(-2, 12, 500)
colores = ['#2E86AB', '#E63946']

for idx, m in enumerate(m_solutions):
    y = f(x_global, m)
    Vx, Vy = calcular_vertice(m)
    
    plt.plot(x_global, y, color=colores[idx], linewidth=2.5, 
             label=f'$m = {m:.0f}$')
    plt.scatter([Vx], [Vy], color=colores[idx], s=150, 
                zorder=5, edgecolors='white', linewidths=2)
    plt.scatter([Vx], [0], color=colores[idx], s=120, 
                zorder=5, marker='s', edgecolors='white', linewidths=1.5)

plt.axhline(y=0, color='#333333', linewidth=1.2, alpha=0.7)
plt.axvline(x=0, color='#333333', linewidth=1.2, alpha=0.7)
plt.xlabel('x', fontsize=12, fontweight='bold')
plt.ylabel('f(x)', fontsize=12, fontweight='bold')
plt.title('Comparación de ambas parábolas tangentes', 
          fontsize=14, fontweight='bold', pad=15)
plt.grid(True, linestyle='--', alpha=0.4, linewidth=0.8)
plt.gca().set_facecolor('#F8F9FA')
plt.legend(loc='upper right', framealpha=0.95, edgecolor='gray', fontsize=10)
plt.tight_layout()
plt.show()