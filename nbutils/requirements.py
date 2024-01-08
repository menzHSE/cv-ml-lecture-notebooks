# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

import os
import sys

from nbutils import exec as nb_exec


def pip_install_reqs(req_file, on_colab):
    # Install requirements in the current Jupyter kernel
    if os.path.exists(req_file):
        command = [sys.executable, "-m", "pip", "install", "-r", req_file]
        nb_exec.executeCommand(command, on_colab)
    else:
        print(f"Requirements file not found: {req_file}")
