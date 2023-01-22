"""Get protein files from PDB server and save locally"""

import os
from Bio.PDB import PDBList


def get_proteins(mol_1=None, mol_2=None):
    # Create directories, if necessary
    if not os.path.exists('src/conftopo/data/tmp'):
        os.makedirs('src/conftopo/data/tmp/biopython')
        os.makedirs('src/conftopo/data/tmp/morph')

    # Retrieve protein files from the PDB server
    pdbl = PDBList()
    pdbl.download_pdb_files([mol_1, mol_2], file_format='pdb',
                            pdir='src/conftopo/data/tmp/biopython')

    # Change specific file names to generic names for importing into ChimeraX
    # os.chdir('src/data/tmp/biopython')
    os.rename('src/conftopo/data/tmp/biopython/pdb'+mol_1+'.ent', 'src/conftopo/data/tmp/biopython/mol_1.ent')
    os.rename('src/conftopo/data/tmp/biopython/pdb'+mol_2+'.ent', 'src/conftopo/data/tmp/biopython/mol_2.ent')
