"""Generate persistence curves for all PDB files."""
import os
import numpy as np
from conftopo.compute_persist_curves import compute_persist_curves

# Loop over PDB files in directory
os.chdir('tmp/morph')
n_files = len(os.listdir())
lcs = np.empty((0, 300), int)
for i in range(1, n_files):
   lc_all = compute_persist_curves('morph_'+str(i)+'.pdb', verbose=1)
   lcs = np.vstack((lcs, lc_all))