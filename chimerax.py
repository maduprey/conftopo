# Call ChimeraX from Python

# Call from terminal (or add from path); in the case of Linux should just be able
# to directly call 'chimerax' in place of the actual path

import subprocess

# Note that the 'shell=True' argument is necessary
subprocess.run(f"/Applications/ChimeraX-1.2.5.app/Contents/MacOS/ChimeraX --nogui morph.cxc", shell=True)