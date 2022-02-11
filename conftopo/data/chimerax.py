"""Perform ChimeraX preprocessing.

1. Deletes everything except for chain A
2. Performs matchmaker to align proteins
3. Generates a 60-frame morph from mol_1 to mol_2
4. Saves each intermediate conformation to a PDB file
"""

import subprocess

# Call from terminal (or add from path); in the case of Linux should just be able
# to directly call 'chimerax' in place of the actual path
#TODO: See if we can write the morphed trajectory to a single PDB file
subprocess.run(f"/Applications/ChimeraX-1.2.5.app/Contents/MacOS/ChimeraX --nogui conftopo/data/morph.cxc", shell=True)