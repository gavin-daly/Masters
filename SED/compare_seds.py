import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

def read_two_column(path):
    """Try to read first two columns (wavelength, flux) from path."""
    try:
        df = pd.read_csv(path, delim_whitespace=True, comment='#', header=None,
                         usecols=[0,1], names=['wavelength','flux'])
        return df['wavelength'].to_numpy(), df['flux'].to_numpy()
    except Exception:
        pass
    try:
        data = np.loadtxt(path, comments='#', usecols=(0,1))
        return data[:,0], data[:,1]
    except Exception as e:
        raise RuntimeError(f"Could not read two-column data from {path}: {e}")

# --- get f1 from argument ---
if len(sys.argv) < 2:
    print("Usage: python compare_seds.py <model_spectrum_file>")
    sys.exit(1)

f1 = sys.argv[1]              # Model file (changes per run)
f2 = "realSED.txt"            # Observed file (fixed)

wl1, fl1 = read_two_column(f1)
wl2, fl2 = read_two_column(f2)
fl1 = fl1 * 1e-6

# Sort
i1 = np.argsort(wl1); wl1, fl1 = wl1[i1], fl1[i1]
i2 = np.argsort(wl2); wl2, fl2 = wl2[i2], fl2[i2]

# Plot
plt.figure(figsize=(8,5))
plt.scatter(wl1, fl1, s=10, label=f"Model SED ({f1})")
plt.scatter(wl2, fl2, s=10, alpha=0.8, label="PDS-415 SED")
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1, 1e+3)
plt.xlabel("Wavelength")
plt.ylabel("Flux")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"comparison_{f1.replace('.','_')}.png")
plt.close()
