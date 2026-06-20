import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.fft import fft, fftfreq

# ------------------------------------------------------------
# Parameters - feel free to tweak these!
# ------------------------------------------------------------
omega1 = 1.0       # Natural frequency of our universe (rad/unit time)
omega2 = 1.2       # Natural frequency of the other universe (slightly different → repulsion)
kappa_max = 5.0    # Maximum coupling strength during bounce
bounce_center = 20.0  # Time when bounce peaks
bounce_width = 4.0    # How sharp/narrow the bounce is (smaller = sharper)

t_start = 0
t_end = 60
t_points = 2000
t = np.linspace(t_start, t_end, t_points)

# Time-dependent coupling: Gaussian peak during "bounce"
def kappa(t):
    return kappa_max * np.exp( - (t - bounce_center)**2 / (2 * bounce_width**2) )

# ------------------------------------------------------------
# System of equations: two coupled oscillators
# State vector y = [x1, v1, x2, v2]
# ------------------------------------------------------------
def coupled_oscillators(y, t):
    x1, v1, x2, v2 = y
    
    k = kappa(t)  # time-varying coupling
    
    # Accelerations
    a1 = -omega1**2 * x1 - k * (x1 - x2)
    a2 = -omega2**2 * x2 - k * (x2 - x1)
    
    return [v1, a1, v2, a2]

# ------------------------------------------------------------
# Initial conditions: both oscillators start at rest, small displacement
# ------------------------------------------------------------
y0 = [1.0, 0.0,   # x1(0) = 1, v1(0) = 0
      0.5, 0.0]   # x2(0) = 0.5, v2(0) = 0   (different starting points)

# Solve the ODE
solution = odeint(coupled_oscillators, y0, t)

x1 = solution[:, 0]
x2 = solution[:, 2]

# ------------------------------------------------------------
# Plot positions over time
# ------------------------------------------------------------
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, x1, label='Our Universe (ω₁ = {})'.format(omega1), linewidth=2)
plt.plot(t, x2, label='Other Universe (ω₂ = {})'.format(omega2), linewidth=2)
plt.title('Positions during Bounce (coupling κ peaks at t={})'.format(bounce_center))
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.grid(True)

# Plot the coupling strength for reference
plt.subplot(2, 1, 2)
plt.plot(t, kappa(t), 'r--', label='Coupling κ(t)', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Coupling Strength κ')
plt.title('Time-dependent Coupling (Bounce)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Bonus: Frequency analysis after the bounce (look for new modes!)
# Take data after bounce (t > bounce_center + 10)
# ------------------------------------------------------------
idx_after = t > (bounce_center + 10)
t_after = t[idx_after]
x1_after = x1[idx_after]

N = len(x1_after)
yf = fft(x1_after)
xf = fftfreq(N, d=t_after[1]-t_after[0])[:N//2]

plt.figure(figsize=(10, 5))
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.title('Frequency Spectrum of Our Universe AFTER Bounce')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.xlim(0, 3)  # zoom in around our expected range
plt.grid(True)
plt.show()
