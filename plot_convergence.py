import pandas as pd
import matplotlib.pyplot as plt
import glob

files = glob.glob('openfoam_rans/postProcessing/forceCoeffs1/*/forceCoeffs.dat')
filepath = files[0]

data = pd.read_csv(filepath, comment='#', sep=r'\s+', header=None,
                    names=['Time', 'Cm', 'Cd', 'Cl', 'Clf', 'Clr'])

time = data['Time'].to_numpy()
cd = data['Cd'].to_numpy()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time, cd, linewidth=1.5, color='#2563eb')
ax.set_xlabel('Iteration', fontsize=12)
ax.set_ylabel('Drag Coefficient (Cd)', fontsize=12)
ax.set_title('Ahmed Body (25 deg Slant) - Cd Convergence History', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.axhline(y=cd[-1], color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
ax.text(time[-1]*0.7, cd[-1]+0.005, f"Converged Cd = {cd[-1]:.4f}", fontsize=10, color='gray')

plt.tight_layout()
plt.savefig('results/ahmed_body_cd_convergence.png', dpi=200, bbox_inches='tight')
print(f"Saved. Final Cd = {cd[-1]:.4f}")
