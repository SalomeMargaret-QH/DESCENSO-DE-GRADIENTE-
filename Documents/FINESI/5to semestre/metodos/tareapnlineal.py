import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Ejercicios de Convexidad y Gráficos",
    page_icon="💜",
    layout="wide"
)

# Estilo de colores personalizados
st.markdown(
    """
    <style>
    .main {background-color: #F0EFFF;}
    div.stButton > button {background-color: #A78BFA; color: white;}
    .stHeader {color: #4F46E5;}
    h1, h2, h3 {color: #4F46E5;}
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.title("💜 Resolución Paso a Paso de Ejercicios de Convexidad 💜")
st.write("Este programa resuelve los ejercicios de convexidad del PDF paso a paso, mostrando gráficos y explicaciones detalladas.")

# Función para graficar
def plot_function(func, x_range, title, deriv=None):
    x_vals = np.linspace(x_range[0], x_range[1], 500)
    y_vals = [func(x) for x in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x)", color="#A78BFA")  # Moradito
    if deriv:
        y_deriv_vals = [deriv(x) for x in x_vals]
        plt.plot(x_vals, y_deriv_vals, label="f''(x)", linestyle="--", color="#E879F9")  # Rosado suave
    plt.axhline(0, color="#4F46E5", linewidth=0.8, linestyle="--")  # Azul oscuro
    plt.title(title, color="#4F46E5")
    plt.xlabel("x", color="#4F46E5")
    plt.ylabel("y", color="#4F46E5")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Ejercicio 1 - Demuestra que f(x) = 3x + 2 es convexa
st.header("Ejercicio 1: \( f(x) = 3x + 2 \)")
st.write("### Resolución Paso a Paso:")
st.latex(r"f(x) = 3x + 2")
st.write("La función es lineal, por lo que es convexa en todo su dominio. Además, su segunda derivada es:")
st.latex(r"f''(x) = 0")
st.write("Esto confirma que es convexa, pero no estrictamente convexa.")
st.write("### Gráfico")
f1 = sp.lambdify(x := sp.Symbol('x'), 3 * x + 2, 'numpy')
plot_function(f1, [-10, 10], "Gráfico de \( f(x) = 3x + 2 \)")

# Ejercicio 2 - Verifique si f(x) = x^3 es convexa en [0, ∞)
st.header("Ejercicio 2: \( f(x) = x^3 \)")
st.write("### Resolución Paso a Paso:")
st.latex(r"f(x) = x^3")
st.write("Calculamos las derivadas:")
f2 = x**3
f2_prime = sp.diff(f2, x)
f2_double_prime = sp.diff(f2_prime, x)
st.latex(f"f'(x) = {sp.latex(f2_prime)}")
st.latex(f"f''(x) = {sp.latex(f2_double_prime)}")
st.write("La segunda derivada es positiva para \( x > 0 \), lo que indica convexidad en este intervalo.")
st.write("### Gráfico")
plot_function(sp.lambdify(x, f2, 'numpy'), [-2, 2], "Gráfico de \( f(x) = x^3 \) y \( f''(x) \)", deriv=sp.lambdify(x, f2_double_prime, 'numpy'))

# Ejercicio 3 - Demostrar que f(x) = e^(2x) es convexa
st.header("Ejercicio 3: \( f(x) = e^{2x} \)")
st.write("### Resolución Paso a Paso:")
st.latex(r"f(x) = e^{2x}")
st.write("Calculamos las derivadas:")
f3 = sp.exp(2 * x)
f3_prime = sp.diff(f3, x)
f3_double_prime = sp.diff(f3_prime, x)
st.latex(f"f'(x) = {sp.latex(f3_prime)}")
st.latex(f"f''(x) = {sp.latex(f3_double_prime)}")
st.write("Dado que \( f''(x) > 0 \) para todo \( x \in \mathbb{R} \), la función es convexa.")
st.write("### Gráfico")
plot_function(sp.lambdify(x, f3, 'numpy'), [-2, 2], "Gráfico de \( f(x) = e^{2x} \) y \( f''(x) \)", deriv=sp.lambdify(x, f3_double_prime, 'numpy'))

# Ejercicio 4 - Verificar si f(x) = ln(x) es convexa o cóncava
st.header("Ejercicio 4: \( f(x) = \ln(x) \)")
st.write("### Resolución Paso a Paso:")
st.latex(r"f(x) = \ln(x)")
st.write("Calculamos las derivadas:")
f4 = sp.log(x)
f4_prime = sp.diff(f4, x)
f4_double_prime = sp.diff(f4_prime, x)
st.latex(f"f'(x) = {sp.latex(f4_prime)}")
st.latex(f"f''(x) = {sp.latex(f4_double_prime)}")
st.write("Dado que \( f''(x) < 0 \) en \( (0, \infty) \), la función es cóncava.")
st.write("### Gráfico")
plot_function(sp.lambdify(x, f4, 'numpy'), [0.1, 5], "Gráfico de \( f(x) = \ln(x) \) y \( f''(x) \)", deriv=sp.lambdify(x, f4_double_prime, 'numpy'))

# Ejercicio 5 - Análisis de \( f(x) = x^4 - 2x^2 + 1 \)
st.header("Ejercicio 5: \( f(x) = x^4 - 2x^2 + 1 \)")
st.write("### Resolución Paso a Paso:")
st.latex(r"f(x) = x^4 - 2x^2 + 1")
st.write("Calculamos las derivadas:")
f5 = x**4 - 2*x**2 + 1
f5_prime = sp.diff(f5, x)
f5_double_prime = sp.diff(f5_prime, x)
st.latex(f"f'(x) = {sp.latex(f5_prime)}")
st.latex(f"f''(x) = {sp.latex(f5_double_prime)}")
critical_points = sp.solve(f5_double_prime, x)
st.write("Los puntos críticos de la segunda derivada son:")
st.latex(f"x = {sp.latex(critical_points)}")
st.write("Estos puntos determinan los intervalos de convexidad y concavidad.")
st.write("### Gráfico")
plot_function(sp.lambdify(x, f5, 'numpy'), [-2, 2], "Gráfico de \( f(x) = x^4 - 2x^2 + 1 \) y \( f''(x) \)", deriv=sp.lambdify(x, f5_double_prime, 'numpy'))

# Footer
st.markdown("---")
st.write("💜 Desarrollado por Salome")
