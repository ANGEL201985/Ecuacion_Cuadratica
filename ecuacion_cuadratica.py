import numpy as np
import matplotlib.pyplot as plt

# ================================
# 1. Hallar m para parábola tangente al eje x
# ================================
coeff = [1, -4, -60]
m_solutions = np.roots(coeff)

print("Soluciones para m (discriminante = 0):")
for m in m_solutions:
    print(f"  m = {m:.2f}")

# ================================
# 2. Definir función y analizar soluciones
# ================================
def f(x, m):
    return x**2 - m*x + m + 15

for m in m_solutions:
    m_val = float(m)
    Vx = m_val / 2
    Vy = f(Vx, m_val)
    print(f"\nPara m = {m_val:.1f}:")
    print(f"  Vértice en ({Vx:.1f}, {Vy:.1f})")
    print(f"  E = m² - m + 1 = {m_val**2 - m_val + 1:.0f}")

# ================================
# 3. Graficar solo para m = 10
# ================================
m_elegido = 10.0
x = np.linspace(-1, 11, 500)
y = f(x, m_elegido)
vert_x = m_elegido / 2
vert_y = f(vert_x, m_elegido)

plt.figure(figsize=(10, 6))

# Graficar parábola
plt.plot(x, y, color='#2E86AB', linewidth=2.5, 
         label=f'$f(x) = x^2 - {m_elegido:.0f}x + {m_elegido + 15:.0f}$')

# Ejes principales
plt.axhline(y=0, color='#333333', linewidth=1.2, linestyle='-', alpha=0.7, label='Eje X')
plt.axvline(x=0, color='#333333', linewidth=1.2, linestyle='-', alpha=0.7)

# Línea vertical al vértice
plt.axvline(x=vert_x, color='#A23B72', linestyle='--', linewidth=1.2, 
            alpha=0.6, label=f'$x = {vert_x:.1f}$')

# Vértice destacado
plt.scatter([vert_x], [vert_y], color='#F18F01', s=150, 
            zorder=5, edgecolors='white', linewidths=2,
            label=f'Vértice $({vert_x:.1f}, {vert_y:.1f})$')

# Punto de tangencia con el eje x
plt.scatter([vert_x], [0], color='#C73E1D', s=120, 
            zorder=5, marker='s', edgecolors='white', linewidths=1.5,
            label='Punto de tangencia')

# Etiquetas y título
plt.xlabel('x', fontsize=12, fontweight='bold')
plt.ylabel('f(x)', fontsize=12, fontweight='bold')
plt.title(f'Parábola tangente al eje X con m = {m_elegido:.0f}', 
          fontsize=14, fontweight='bold', pad=15)

# Grid y fondo
plt.grid(True, linestyle='--', alpha=0.4, linewidth=0.8)
plt.gca().set_facecolor('#F8F9FA')

# Leyenda
plt.legend(loc='upper right', framealpha=0.95, edgecolor='gray', fontsize=10)

# Ajustar límites
y_min, y_max = min(y), max(y)
margin = (y_max - y_min) * 0.1
plt.ylim([y_min - margin, y_max + margin])

plt.tight_layout()
plt.show()

# ================================
# 4. Calcular E para m = 10
# ================================
E = m_elegido**2 - m_elegido + 1
print("\n" + "="*50)
print("RESULTADO FINAL:")
print("="*50)
print(f"Para m = {m_elegido:.0f}: E = m² - m + 1 = {E:.0f}")