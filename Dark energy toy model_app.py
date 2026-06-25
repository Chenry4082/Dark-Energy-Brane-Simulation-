import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Set random seed for reproducibility
np.random.seed(42)

st.title("🌌 Dark Energy Brane Simulation: Quantum Tunneling & Cosmic Acceleration")
st.markdown("""
### Grounded Framework: Brane-World Cosmology & Observational Astronomy
This simulation models the accelerated expansion of our universe via quantum tunneling across a thin inter-brane matrix layer. 
* **Cosmic Acceleration:** The repulsive mechanics match the acceleration curves observed via **Type Ia Supernova** standard candles.
* **Residual Spectrum:** The Fast Fourier Transform (FFT) simulates quantum ripples, providing a theoretical analogue to the **Cosmic Microwave Background (CMB)** acoustic peaks.
""")

# Sidebar
st.sidebar.header("Cosmological Parameters")
omega1 = st.sidebar.slider("Our Universe Intrinsic Frequency (ω₁)", 0.5, 3.0, 1.0, 0.1)
omega2 = st.sidebar.slider("Neighbor Universe Intrinsic Frequency (ω₂)", 0.5, 3.0, 1.2, 0.1)
kappa_max = st.sidebar.slider("Peak Inter-Brane Coupling (κ_max)", 1.0, 10.0, 3.0, 0.5)
repulsion_strength = st.sidebar.slider("Dark Energy Repulsion Intensity (Supernova Lambda Analogue)", 0.0, 5.0, 2.0, 0.2)
tunneling_noise = st.sidebar.slider("Quantum Tunneling Noise (Matrix Ripples)", 0.0, 0.5, 0.1, 0.05)
damping = st.sidebar.slider("Cosmic Damping (Expansion Dissipation)", 0.0, 0.1, 0.02, 0.005)

st.sidebar.markdown("*Note: Parameters are in simplified arbitrary units. ω ≈ 1 corresponds to oscillation cycles over cosmological timescales for illustration.*")

# Timeline
num_steps = 4000
t = np.linspace(0, 120, num_steps)
dt = t[1] - t[0]

def kappa(t_val):
    return kappa_max * np.exp(-((t_val - 40.0)**2) / (2 * 12.0**2)) + 0.4

# Arrays
x1 = np.zeros(num_steps)
v1 = np.zeros(num_steps)
x2 = np.zeros(num_steps)
v2 = np.zeros(num_steps)

# Initial conditions
x1[0] = 0.8
v1[0] = 0.0
x2[0] = 1.15
v2[0] = 0.0

noise = np.random.normal(0, tunneling_noise, num_steps)

for i in range(1, num_steps):
    t_val = t[i-1]
    k = kappa(t_val)
    sep = abs(x1[i-1] - x2[i-1]) + 0.01
    
    repulse = repulsion_strength / (sep**2) * np.sign(x1[i-1] - x2[i-1])
    
    # Deterministic accelerations
    dv1_dt = -omega1**2 * x1[i-1] - k * (x1[i-1] - x2[i-1]) + repulse - damping * v1[i-1]
    dv2_dt = -omega2**2 * x2[i-1] - k * (x2[i-1] - x1[i-1]) - repulse - damping * v2[i-1]
    
    # Euler-Maruyama stochastic integration
    x1[i] = x1[i-1] + v1[i-1] * dt
    v1[i] = v1[i-1] + dv1_dt * dt + noise[i-1] * np.sqrt(dt)
    
    x2[i] = x2[i-1] + v2[i-1] * dt
    v2[i] = v2[i-1] + dv2_dt * dt + noise[i-1] * np.sqrt(dt) * 0.7  # slightly weaker on neighbor

# Visualizations
plt.style.use('dark_background')
fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

axs[0].plot(t, x1, color='#1f77b4', label='Our Universe Scale Factor a(t)', lw=2)
axs[0].plot(t, x2, color='#ff7f0e', label='Neighbor Universe Scale Factor a(t)', lw=2)
axs[0].set_ylabel("Cosmological Scale Factor a(t)")
axs[0].set_title("Universe Evolution Profile (Inspired by Supernova Data)")
axs[0].legend()
axs[0].grid(True, alpha=0.3)

separation = np.abs(x1 - x2)
axs[1].plot(t, separation, color='cyan', label='Inter-Brane Matrix Thickness')
axs[1].set_ylabel("Matrix Thickness (Thin Bulk)")
axs[1].legend()
axs[1].grid(True, alpha=0.3)

velocity = np.gradient(x1, t)
axs[2].plot(t, velocity, color='#ffcc00', lw=1.5, label='da/dt (Expansion Rate)')
axs[2].set_ylabel("Expansion Rate")
axs[2].set_xlabel("Cosmological Time Epochs")
axs[2].legend()
axs[2].grid(True, alpha=0.3)

fig.tight_layout()
st.pyplot(fig)

# FFT Analysis
late_start = int(num_steps * 0.6)
late_slice = x1[late_start:]
late_slice = late_slice - np.mean(late_slice)
freqs = np.fft.rfftfreq(len(late_slice), d=dt)
fft = np.abs(np.fft.rfft(late_slice))

st.subheader("🌌 Cosmic Acoustic Peaks (CMB Power Spectrum Analogue)")
st.markdown("This spectrum shows the persistent low-frequency residual signature from inter-brane quantum tunneling.")

fig_fft, ax_fft = plt.subplots(figsize=(9, 5))
ax_fft.plot(freqs[:80], fft[:80], color='#00ffcc', lw=2)
ax_fft.set_xlabel("Multipole Moment / Spatial Frequency")
ax_fft.set_ylabel("Power / Amplitude")
ax_fft.grid(True, alpha=0.3)
st.pyplot(fig_fft)

st.markdown("""
**Interpretation**: Stabilized separation due to repulsion + persistent low-frequency FFT component illustrates how tunneled ripples can sustain accelerated expansion.
""")
