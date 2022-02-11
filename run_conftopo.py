"""Generate persistence curves for all PDB files."""

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
    os.chdir(dir)
    n_files = len(os.listdir())
    lcs = np.empty((0, 300), int)
    for i in range(1, n_files):
        lc_all = compute_persist_curves('morph_'+str(i)+'.pdb', verbose=1)
        lcs = np.vstack((lcs, lc_all))

    return(lcs)


def main():
    get_proteins('1klq', '1duj')
    chimerax()
    print(os.getcwd())
    lcs = compute_conf_pc('conftopo/data/tmp/morph')

    # Compute across H_0, H_1, and H_2
    homology = range(000, 300)

    # Compute L^2 norm
    dist = []
    for k in range(60):
        dist.append(np.linalg.norm(lcs[0, homology] - lcs[k, homology]))

    # Plot
    plt.subplots(figsize=(12, 6))
    plt.title("$L^2$ norm between persistence curves for conformations)")
    plt.xlabel("Conformation")
    plt.ylabel("$L^2$ norm")
    plt.plot(dist)
    # plt.show()
    plt.savefig('conftopo/data/graph.png')


if __name__ == '__main__':
    main()
