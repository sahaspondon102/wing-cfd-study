# Case conditions
rho = 1.225          # kg/m^3, freestream density
mu = 1.7894e-5        # kg/(m.s), dynamic viscosity
U_inf = 30.0          # m/s, freestream velocity
chord = 0.2           # m, reference chord length
y_plus_target = 1.0   # target y+ for first cell

# Reynolds number based on chord
Re_c = rho * U_inf * chord / mu

# Flat-plate turbulent skin friction coefficient (Schlichting correlation)
Cf = 0.058 * Re_c ** -0.2

tau_w = 0.5 * Cf * rho * U_inf ** 2
u_tau = (tau_w / rho) ** 0.5

y1 = y_plus_target * mu / (rho * u_tau)

# inflation layer stack (5 layers @ 1.2 growth)
n_layers = 5
growth_rate = 1.2

layer_heights = [y1 * growth_rate ** i for i in range(n_layers)]
stack_thickness = sum(layer_heights)

if __name__ == "__main__":
    print(f"Re_c                 = {Re_c:.3e}")
    print(f"Cf (flat plate)      = {Cf:.5f}")
    print(f"tau_w                = {tau_w:.5f} Pa")
    print(f"u_tau                = {u_tau:.5f} m/s")
    print(f"y1 (first cell ht)   = {y1*1000:.5f} mm")
    print()
    print(f"Prism stack ({n_layers} layers, growth {growth_rate}):")
    print(f"  total stack thickness = {stack_thickness*1000:.3f} mm")
    print(f"  last layer thickness  = {layer_heights[-1]*1000:.3f} mm")