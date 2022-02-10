"""Compute persistence curves."""

import os
import numpy as np
import persistencecurves as pc
from Bio.PDB import PDBParser
from ripser import ripser
 
def compute_persist_curves(file=None):
    """
    Compute persistence curves -- normalized life curves -- using the atomic 
    positions as a point cloud.
    
    Arguments:
        file: A PDB file.
        
    Returns:
        A one-dimensional numpy array containing the concatenated normalized
        life curves for H_0, H_1, and_H_2, corresponding to positions [0, 99],
        [100, 199], and [200, 299], respectively.
    """
    
    parser = PDBParser(PERMISSIVE=1, QUIET=True)
    structure = parser.get_structure(file, file)
    
    # Generate a list of the R^3 coordinates for all of the protein's atoms
    coords = []
    for atom in structure.get_atoms():
        coords.append(list(atom.get_vector()))
    coords = np.array(coords)
    
    # Compute persistent homology
    if len(coords) > 1300:
        diagram = ripser(coords, maxdim=2, thresh=10, do_cocycles=False, n_perm=1300)['dgms']
    else:
        diagram = ripser(coords, maxdim=2, thresh=10, do_cocycles=False)['dgms']

    # Generate persistence curves from diagrams
    d_h0 = pc.Diagram(Dgm=diagram[0], globalmaxdeath=10, inf_policy='remove')
    d_h1 = pc.Diagram(Dgm=diagram[1], globalmaxdeath=10, inf_policy='remove')
    d_h2 = pc.Diagram(Dgm=diagram[2], globalmaxdeath=10, inf_policy='remove')

    # Generate normalized life curve
    lc_h0 = d_h0.lifecurve(meshstart=0, meshstop=10, num_in_mesh=100)
    lc_h1 = d_h1.lifecurve(meshstart=0, meshstop=10, num_in_mesh=100)
    lc_h2 = d_h2.lifecurve(meshstart=0, meshstop=10, num_in_mesh=100)

    # Concatenate life curves for a particular conformation
    lc_all = np.concatenate((lc_h0, lc_h1, lc_h2))
    return(lc_all)