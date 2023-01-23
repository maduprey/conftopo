import shutil
import filecmp

from conftopo.data.get_proteins import get_proteins
from conftopo.data.chimerax import chimerax
# from conftopo.compute_persist_curves import compute_persist_curves

# Delete residual data
shutil.rmtree('src/conftopo/data/tmp')


def test_get_proteins():
    get_proteins(mol_1='1cm1', mol_2='1cfd', path='src/conftopo/data/tmp/biopython')
    expected_1 = 'tests/test_data/mol_1.ent'
    expected_2 = 'tests/test_data/mol_2.ent'
    actual_1 = 'src/conftopo/data/tmp/biopython/mol_1.ent'
    actual_2 = 'src/conftopo/data/tmp/biopython/mol_2.ent'
    assert filecmp.cmp(actual_1, expected_1), "Molecule 1 equivalent."
    assert filecmp.cmp(actual_2, expected_2), "Molecule 2 equivalent."


def test_chimerax():
    """Test to see if morphing in ChimeraX is working anticipated."""
    chimerax()
    expected = 'tests/test_data/morph.pdb'
    actual = 'src/conftopo/data/tmp/morph/morph.pdb'
    assert filecmp.cmp(actual, expected), "Morph equivalent."

