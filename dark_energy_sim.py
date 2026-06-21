import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Page setup
st.title("🌌 Dark Energy Brane Simulation Dashboard")
st.markdown("Interact with the sliders in the sidebar to morph the framework live.")

# Sidebar variables
omega1 = st.sidebar.slider("Our Universe Frequency (ω1)", 0.5, 3.0, 1.0, 0.1)
omega2 = st.sidebar.slider("Neighboring Universe Frequency (ω2)", 0.5, 3.0, 1.2, 0.1)
kappa_max = st.sidebar.slider("Max Coupling (κ_max)", 1.0, 10.0, 5.0, 0.5)

# Physics calculations
t = np.linspace(0, 60, 2000)
def kappa(t_val):
    return kappa_max * np.exp(-((t_val - 20.0) ** 2) / (2 * 4.0 ** 2))

def coupled_oscillators(y, t_val):
    x1, v1, x2, v2 = y
    k = kappa(t_val)
    return [v1, -omega1**2 * x1 - k * (x1 - x2), v2, -omega2**2 * x2 - k * (x2 - x1)]

solution = odeint(coupled_oscillators, [1.0, 0.0, 0.5, 0.0], t)

# Building the visual plot
fig, ax = plt.subplots(figsize=(10, 5))
plt.style.use('dark_background')
ax.plot(t, solution[:, 0], color='#1f77b4', label='Our Universe', lw=2)
ax.plot(t, solution[:, 2], color='#ff7f0e', label='Neighboring Universe', lw=2)
ax.grid(True, alpha=0.3)
ax.legend()

# CRITICAL: Tell Streamlit to render the plot on the web screen
st.pyplot(fig)

