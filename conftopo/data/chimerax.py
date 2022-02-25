"""Perform ChimeraX preprocessing.

1. Deletes everything except for chain A
2. Performs matchmaker to align proteins
3. Generates a 60-frame morph from mol_1 to mol_2
4. Saves each intermediate conformation to a PDB file
"""
import subprocess
import platform


def chimerax():
    """
    Call ChimeraX from terminal.
    Note: 
        If you are running macOS and your version of ChimeraX is not 1.2.5 or it 
        is installed somewhere else, adjust the path below.
    """
    if platform.system() == 'Darwin':
        chimerax_path = '/Applications/ChimeraX-1.2.5.app/Contents/MacOS/ChimeraX'
    else:
        chimerax_path = 'chimerax'
    subprocess.run(
        f'{chimerax_path} --nogui conftopo/data/morph.cxc', shell=True)
