# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

import os
import subprocess
import threading
import subprocess
import fcntl
import errno


def executePythonScript(script_path, params, on_colab):  
    if os.path.exists(script_path):
        print(f"Executing script: {script_path}")
        # Create the command list starting with Python and the script path
        command = ["python", script_path]  
         # Add additional arguments from the params dictionary
        if params:
            for key, value in params.items():
                command.append(f"--{key}")
                command.append(str(value))
        executeCommand(command, on_colab)
    else:
        print(f"Script not found: {script_path}")    



def executeCommand(command, on_colab):
    if on_colab:
        executeCaptureColabCommand(command)     
    else:
        executeCaptureCommand(command)    
   

def executeCaptureCommand(command):   
    print(command)
    subprocess.run(command)

# This is very hacky ... but it's hard to capture the output of a subprocess in Colab
def executeCaptureColabCommand(command):  

        print(command) 
    
        # Start the subprocess
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Set the stdout to non-blocking
        fd = process.stdout.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

        # Function to continuously output lines from a stream
        def stream_output(stream):
            while True:
                try:
                    line = stream.readline()
                    if line:
                        print(line, end='')
                    elif process.poll() is not None:
                        break
                except IOError as e:
                    # Ignore the error if no data is available yet
                    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                        raise

        # Use a thread to capture the output stream
        output_thread = threading.Thread(target=stream_output, args=(process.stdout,))
        output_thread.start()

        # Wait for the subprocess to complete and the output thread to end
        process.wait()
        output_thread.join()

