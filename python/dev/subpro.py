import subprocess
import appscript
import os

#appscript.app('Terminal').do_script('ls')

#appscript.Application('/Applications/iTerm.app').launch()



subprocess.run(['/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal'], shell=True).poll()

