# Dark Energy Brane Simulation

### **Abstract**
This interactive simulation explores a cyclical brane-world framework in which **dark energy** emerges as the sustained effect of "ripples" leaking between neighboring branes via quantum tunneling in a thin bulk.

**Core Picture**: Imagine an infinite bowl of cereal — countless Trix-like brane "universes" expanding (Big Bang phase) and contracting (Big Bounce phase) in cycles. These branes sit very close together (thin bulk), appearing nearly touching to the naked eye yet repelling each other through a stabilizing force. Ripples in the "milk" (higher-dimensional bulk) squeeze through the narrow gaps via quantum tunneling, delivering a small but persistent energy influx. This creates a nearly constant outward push — the observed accelerated expansion we attribute to dark energy.

The model is a **classical coupled-oscillator toy simulation** inspired by real ideas in brane cosmology and ekpyrotic/cyclic models. It is not a full quantum-gravity or 5D GR solution, but a helpful visualization for intuition-building.

---

### **Key Concepts**
- **Cyclic Branes**: Each universe oscillates between expansion and contraction phases.
- **Thin Bulk + Repulsion**: Branes hover near one another with a short-range repulsive barrier (modeled as ~1/separation²) that prevents full merger while allowing ongoing gentle interactions.
- **Quantum Tunneling Ripples**: Stochastic noise in the simulation represents small energy/momentum leaks across the thin separation, sustaining a residual low-frequency "hum" that drives accelerated expansion.
- **Big Bounce**: Occasional closer approaches during oscillations trigger chaotic but brief energy exchange without singularities.

---

### **Simulation Features**
- Fully interactive Streamlit app with sliders for frequencies, coupling, repulsion strength, and tunneling amplitude.
- Visualizes brane positions, separation dynamics, velocity (expansion intuition), and the post-interaction Fourier spectrum.
- Demonstrates how near-contact repulsion stabilizes the system while tunneling maintains a persistent effect.

**[Launch Interactive Demo]** (update with your current Streamlit link)

---

### **How to Run Locally**
```bash
git clone https://github.com/Chenry4082/Dark-Energy-Brane-Simulation-.git
cd Dark-Energy-Brane-Simulation-
pip install -r requirements.txt
streamlit run dark_energy_sim.py
