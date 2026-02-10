import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import api
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api.engine.linear import check_disturbance_decoupling, compute_feedback_matrix

def generate_ddp_plot():
    # System definitions
    # A = [[0, 1], [2, 0]]
    # B = [[0], [1]]
    # C = [[1, -1]]
    # E = [[1], [1]]
    
    A = np.array([[0.0, 1.0], [2.0, 0.0]])
    B = np.array([[0.0], [1.0]])
    C = np.array([[1.0, -1.0]])
    E = np.array([[1.0], [1.0]])
    
    # Check DDP
    is_solvable, V_star, F = check_disturbance_decoupling(A, B, E, C)
    
    if not is_solvable:
        print("DDP not solvable for example system!")
        return
        
    # Simulation
    dt = 0.01
    T = 10.0
    steps = int(T / dt)
    time = np.linspace(0, T, steps)
    
    # Disturbance
    d = np.sin(2 * np.pi * 0.5 * time) # 0.5 Hz sine wave
    
    # 1. Uncontrolled Simulation (F=0)
    x = np.zeros(2)
    y_uncontrolled = []
    
    for k in range(steps):
        # dot(x) = Ax + Ed
        dx = A @ x + E.flatten() * d[k]
        x = x + dx * dt
        y_val = C @ x
        y_uncontrolled.append(y_val[0])
        
    # 2. Controlled Simulation (F computed)
    x = np.zeros(2)
    y_controlled = []
    
    # Closed loop A
    A_cl = A + B @ F
    
    for k in range(steps):
        # dot(x) = (A+BF)x + Ed
        dx = A_cl @ x + E.flatten() * d[k]
        x = x + dx * dt
        y_val = C @ x
        y_controlled.append(y_val[0])
        
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.style.use('ggplot')
    
    plt.subplot(2, 1, 1)
    plt.plot(time, d, 'k--', label='Disturbance d(t)')
    plt.title('Disturbance Signal')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(time, y_uncontrolled, 'r-', label='Output (Open Loop)')
    plt.plot(time, y_controlled, 'b-', linewidth=2, label='Output (DDP Control)')
    plt.title('System Output y(t)')
    plt.xlabel('Time (s)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../public/graphs/ddp_demo.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150)
    print(f"Graph saved to {output_path}")

if __name__ == "__main__":
    generate_ddp_plot()
