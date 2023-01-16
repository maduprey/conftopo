"""Compute persistence curves."""

import os
import numpy as np
import persistencecurves as pc
from Bio.PDB import PDBParser, Selection
from ripser import ripser


def compute_persist_curves(file=None, verbose=0, n_perm=1300):
    """
    Compute persistence curves -- normalized life curves -- using the atomic 
    positions as a point cloud.

    Arguments:
        file: A multi-model PDB file containing 'm' models of intermediate 
        positions between two conformational states.

        verbose: Prints '<Model id=x>: Done' to console, for each completed 
        persistence curve.

        n_perm: From Ripser, the number of points (atoms) to subsample in a 
        “greedy permutation.”

    Returns:
       A 1xm-dimensional numpy array containing the concatenated normalized
       life curves for H_0, H_1, and_H_2, corresponding to positions [0, 99],
       [100, 199], and [200, 299], respectively, across the 'm' models.
    """

    parser = PDBParser(PERMISSIVE=1, QUIET=True)
    structure = parser.get_structure(file, file)
    model_list = Selection.unfold_entities(structure, "M")

    lcs = np.empty((0, 300), int)
    for model in model_list:
        # Generate a list of the R^3 coordinates for all of the protein's atoms
        coords = []
        for atom in model.get_atoms():
            coords.append(list(atom.get_vector()))
        coords = np.array(coords)

        # Compute persistent homology
        if len(coords) > n_perm:
            diagram = ripser(coords, maxdim=2, thresh=10,
                             do_cocycles=False, n_perm=n_perm)['dgms']
        else:
            diagram = ripser(coords, maxdim=2, thresh=10,
                             do_cocycles=False)['dgms']

        # Generate persistence curves from diagrams
        d_h0 = pc.Diagram(
            Dgm=diagram[0], globalmaxdeath=10, inf_policy='remove')
        d_h1 = pc.Diagram(
            Dgm=diagram[1], globalmaxdeath=10, inf_policy='remove')
        d_h2 = pc.Diagram(
            Dgm=diagram[2], globalmaxdeath=10, inf_policy='remove')

        # Generate normalized life curve
        lc_h0 = d_h0.lifecurve(meshstart=0, meshstop=10, num_in_mesh=100)
        lc_h1 = d_h1.lifecurve(meshstart=0, meshstop=10, num_in_mesh=100)
        lc_h2 = d_h2.lifecurve(meshstart=0, meshstop=10, num_in_mesh=100)

        # Concatenate life curves for a particular conformation
        lc_all = np.concatenate((lc_h0, lc_h1, lc_h2))

        # Aggregate life curves for all conformations
        lcs = np.vstack((lcs, lc_all))

        # Print progress to console
        if verbose == 1:
            print(str(model)+': Done')

    return lcs
