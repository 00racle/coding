import subprocess
import appscript
import os

#appscript.app('Terminal').do_script('ls')

#appscript.Application('/Applications/iTerm.app/Contents/MacOS/iTerm2').launch()

#subprocess.run(['/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal'], shell=True)

#subprocess.run(['/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal', 'ls'], shell=True)

#subprocess.run(["/Applications/iTerm.app/Contents/MacOS/iTerm2", "ls"])

#subprocess.Popen(["/usr/bin/open", "-n", "-a", "/Applications/iTerm.app/Contents/MacOS/iTerm2", "--args", 'ls'])

#subprocess.Popen(["/usr/bin/open -n -a /Applications/iTerm.app/Contents/MacOS/iTerm2 --args ls"] , shell=True, stdout=subprocess.PIPE)

subprocess.Popen(["/usr/bin/open -n -a /Applications/iTerm.app/Contents/MacOS/iTerm2 --args \
                    python3 /Users/ORACLE/testenv/envdir/git/coding/python/dev/hello.py"], shell=True)