"""Get protein files from PDB server and save locally"""

import os
from Bio.PDB import PDBList

# Create directories, if necessary
if not os.path.exists('tmp'):
    os.makedirs('tmp/biopython')
    os.makedirs('tmp/morph')

# Set proteins
mol_1 = '1cm1'
mol_2 = '1cfd'

# Retrieve protein files from the PDB server
pdbl = PDBList()
pdbl.download_pdb_files([mol_1, mol_2], file_format='pdb', pdir='tmp/biopython')

# Change specific file names to generic names for importing into ChimeraX
os.chdir('tmp/biopython')
os.rename('pdb'+mol_1+'.ent', 'mol_1.ent')
os.rename('pdb'+mol_2+'.ent', 'mol_2.ent')