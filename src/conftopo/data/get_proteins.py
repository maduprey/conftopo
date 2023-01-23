"""Get protein files from PDB server and save locally"""

import os
from Bio.PDB import PDBList


def get_proteins(mol_1=None, mol_2=None, path=None):
    # Create directories, if necessary
    if not os.path.exists(path): 
        os.makedirs(path)

    # Retrieve protein files from the PDB server
    pdbl = PDBList()
    pdbl.download_pdb_files([mol_1, mol_2], file_format='pdb',
                            pdir=path)

    # Change specific file names to generic names for importing into ChimeraX
    # os.chdir('src/data/tmp/biopython')
    os.rename(os.path.join(path, 'pdb'+mol_1+'.ent'), os.path.join(path, 'mol_1.ent'))
    os.rename(os.path.join(path, 'pdb'+mol_2+'.ent'), os.path.join(path, 'mol_2.ent'))
