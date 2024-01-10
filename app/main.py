import subprocess
import sys
import tempfile
import os
import shutil

def main():

    # Retrieving the command and its arguments from the command-line arguments
    command = sys.argv[3]
    args = sys.argv[4:]

    # subprocess.run executes the specified command with the provided arguments   
    #completed_process = subprocess.run([command, *args], capture_output=True) # .Popen gives you more control over a subprocess than .run
    #print(completed_process.stdout.decode("utf-8"))
    
    # Creating a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir_path:
        #If command is, for example, "/path/to/myprogram", then binary_name will be assigned the value "myprogram".
        binary_name = os.path.basename(command)
        temp_binary_path = os.path.join(temp_dir_path, binary_name)
        # Copy the executable to the temporary binary path
        shutil.copy2(command, temp_binary_path)
        # Obtain a file descriptor for the root directory and save it in the variable real_root(The primary purpose of obtaining the file descriptor for the root directory is to have a reference to it before performing a chroot operation)
        real_root = os.open("/", os.O_RDONLY)

        try:
            # Change the root directory of the current process to the temporary directory
            os.chroot(temp_dir_path)
            #  Change the current working directory to the root directory ('/')
            os.chdir('/')
            # Execute the command
            completed_process = subprocess.Popen(
                [f"./{binary_name}", *args],
                 capture_output = False
            )
            # stdout, stderr = completed_process.communicate()

            # sys.stdout.write(stdout.decode("utf-8"))
            # sys.stderr.write(stderr.decode("utf-8"))

            # # Execute with the command's return code
            # sys.exit(completed_process.returncode)
        
        except Exception as e:
            print(f"An error occurred {e}")
            sys.exit(1)

        finally:
            # Change the current working directory back to the original root directory
            os.fchdir(real_root)
            # Change the root directory back to the original root
            os.chroot(".")
            # Close the file descriptor for the original root directory.
            os.close(real_root)

if __name__ == "__main__":
    main()
