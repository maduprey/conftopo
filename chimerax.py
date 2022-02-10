# Call ChimeraX from Python

# Call from terminal (or add from path); in the case of Linux should just be able
# to directly call 'chimerax' in place of the actual path

import subprocess

mol_1 = '1cfd'
mol_2 = '1cm1'

# Note that the 'shell=True' argument is necessary
subprocess.run(f"/Applications/ChimeraX-1.2.5.app/Contents/MacOS/ChimeraX --nogui --cmd 'open {mol}; addh; save {mol}.addh.cif; exit'", shell=True)
subprocess.run(f"/Applications/ChimeraX-1.2.5.app/Contents/MacOS/ChimeraX --cmd 'open {mol}; addh'", shell=True)
subprocess.run(f"/Applications/ChimeraX-1.2.5.app/Contents/MacOS/ChimeraX --nogui --cmd 'open {mol_1}; open {mol_2}; del ~ /a; mmaker #1 to #2; morph #1, 2 frames 60; coordset #3, 1,60 ; perframe 'save {mol_1}_{mol_2}_$1.pdb' frames 60; exit'", shell=True)

open 1cfd
open 1cm1
del ~ /a
mmaker #1 to #2
morph #1, 2 frames 60
coordset #3, 1,60 ; perframe "save model_$1.pdb" frames 60

# Currently having issues with the perframe save step
/Applications/ChimeraX-1.2.5.app/Contents/MacOS/ChimeraX --cmd 'open 1cfd; open 1cm1; del ~ /a; mmaker #1 to #2; morph #1, 2 frames 60; coordset #3, 1,60 ; perframe 'save a_b_$1.pdb' frames 60'