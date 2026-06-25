# Dark Energy Brane Simulation: Quantum Tunneling & Cosmic Acceleration

### **Abstract**
This interactive simulation explores a cyclical thin-bulk braneworld framework where **dark energy** emerges from persistent quantum-tunneled ripples between neighboring branes.

**Core Picture**: An infinite bowl of cereal — countless oscillating brane universes in a thin bulk, repelling each other while leaking energy via quantum tunneling. The resulting residual low-frequency "hum" drives sustained accelerated expansion.

---

### **Key Concepts**
- Cyclic oscillations with thin-bulk repulsion.
- Stochastic quantum tunneling modeled via proper **Euler-Maruyama** integration.
- Cosmological mapping: `x(t)` ≈ scale factor `a(t)`.

---

### **Simulation Features**
- **Euler-Maruyama Stochastic Solver**: Rigorous numerical treatment of quantum noise (scaled by √Δt) for reproducible, physically consistent results.
- Three synchronized plots: scale factor evolution, inter-brane separation, and expansion rate (da/dt).
- Late-time FFT showing persistent low-frequency residual (CMB analogue).

**[Launch Interactive Demo]** (update link)

---

### **How to Run Locally**
```bash
git clone https://github.com/Chenry4082/Dark-Energy-Brane-Simulation-.git
cd Dark-Energy-Brane-Simulation-
pip install -r requirements.txt
streamlit run dark_energy_sim.py
