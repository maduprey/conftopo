"""Create plot of L^2 norm between persistence curves of conformation between an
initial and terminal conformation."""

import os
import numpy as np
import matplotlib.pyplot as plt
from conftopo.common.compute_persist_curves import compute_persist_curves
from conftopo.data.get_proteins import get_proteins
from conftopo.data.chimerax import chimerax


def compute_conf_pc(dir=None):
    """
    Compute persistence curves over a full conformational change between two
    conformations.

    Arguments:
       file: A directory containing 'm' ordered PDB files of intermediate positions
       between two conformational states.

    Returns:
       A 1xm-dimensional numpy array containing the concatenated normalized
       life curves for H_0, H_1, and_H_2, corresponding to positions [0, 99],
       [100, 199], and [200, 299], respectively, across the 'm' PDB files.
    """

    # Loop over PDB files in directory
    n_files = len(os.listdir(dir))
    lcs = np.empty((0, 300), int)
    for i in range(1, n_files+1):
        lc_all = compute_persist_curves(dir+'/morph_'+str(i)+'.pdb', verbose=1)
        lcs = np.vstack((lcs, lc_all))

    return(lcs)


def main():
    mol_1 = '2e2n'
    mol_2 = '2e2q'

    get_proteins(mol_1, mol_2)
    chimerax()
    lcs = compute_conf_pc('conftopo/data/tmp/morph')

    # Set plotting range to H_0, H_1, and H_2
    homology = range(000, 300)

    # Compute L^2 norm
    dist = []
    for k in range(len(lcs)):
        dist.append(np.linalg.norm(lcs[0, homology] - lcs[k, homology]))

    # Plot
    plt.figure()
    plt.subplots(figsize=(12, 6))
    plt.title(
        "$L^2$ norm between persistence curves for conformations "+mol_1+" to "+mol_2)
    plt.xlabel("Conformation")
    plt.ylabel("$L^2$ norm")
    plt.plot(dist)
    plt.savefig('conftopo/data/norm_plot_'+mol_1+"_"+mol_2+'.png')


if __name__ == '__main__':
    main()
