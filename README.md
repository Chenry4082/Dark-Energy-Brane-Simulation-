# 🌌 Dark Energy Brane Simulation: Quantum Tunneling & Cosmic Acceleration

This repository contains a 2D cosmological simulation exploring a multi-brane universe framework. Moving away from standard decaying scalar fields, this model simulates accelerated cosmic expansion through **stochastic quantum tunneling** across a highly compactified, thin inter-brane matrix.

The visual interface is built with Streamlit and uses advanced stochastic numerical integration to ensure stability under high quantum fluctuations.

---

## 🔬 Core Physics & Mathematical Formulation

Instead of relying on a deterministic fluid model, the simulation utilizes the **Euler-Maruyama method** for stochastic differential equations (SDEs) to model the transmission of field perturbations between two adjacent branes separated by a thin matrix layer.

### 1. Inter-Brane Coupling ($\kappa(t)$)

As universes or "branes" navigate the compact bulk phase, their interaction strength is epoch-dependent, modeled via a transient Gaussian profile overlaid on a constant baseline matrix potential:


$$\kappa(t) = \kappa_{\max} \exp\left( -\frac{(t - t_0)^2}{2\sigma^2} \right) + \kappa_{\text{baseline}}$$

### 2. Astrophysical Repulsion (Dark Energy Analogue)

The localized matrix dynamics induce a repulsive boundary force that varies inversely with the square of the inter-brane separation distance ($sep$), closely matching the cosmic acceleration curves mapped by astronomers using **Type Ia Supernova** standard candles:


$$F_{\text{rep}} = \frac{\text{repulsion\_strength}}{sep^2 + 0.01} \times \text{sgn}(x_1 - x_2)$$

### 3. Cosmic Damping & Friction

To model the natural energy dissipation and dilution fields undergo over cosmological timescales (akin to Hubble friction), a physical damping term is introduced to steady the expansion velocity:


$$F_{\text{damping}} = -\gamma \cdot v$$

### 4. Stochastic Quantum Tunneling Injection

Real-world quantum fluctuations are represented by adding Gaussian noise scaled mathematically by $\sqrt{dt}$ to preserve physical scaling during time-series integration:


$$v_1(t + dt) = v_1(t) + \frac{dv_1}{dt}dt + \mathcal{N}(0, \sigma_{\text{noise}})\sqrt{dt}$$

---

## 📊 Key Visualizations Explained

The simulation generates three real-time charts mapping the results directly to modern observational astronomy:

* **Cosmological Scale Factor $a(t)$ Profile:** Tracks the size evolution of our universe vs. its neighbor. The curve simulates real expansion metrics inspired by **Supernova Hubble diagrams**.
* **Inter-Brane Matrix Thickness:** Illustrates how the "thin bulk" matrix expands and stabilizes under the influence of the repulsion force.
* **Expansion Velocity ($da/dt$):** The first derivative of the scale factor, acting as a direct analogue to the **Hubble Parameter ($H$)** to chart the changing acceleration rates across different epochs.
* **Cosmic Acoustic Peaks (CMB Spectrum Analogue):** Applies a Fast Fourier Transform (FFT) with signal detrending onto late-stage universe data. The resulting low-frequency peaks provide a beautiful visual analogue to the acoustic anisotropy peaks observed by the Planck Satellite in the **Cosmic Microwave Background (CMB)**.

