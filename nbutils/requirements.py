# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

import os
import sys
import subprocess

def pip_install_reqs(req_file):
    # Install requirements in the current Jupyter kernel  
    if os.path.exists(req_file):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', req_file])
    else:
        print(f"Requirements file not found: {req_file}")