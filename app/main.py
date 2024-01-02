import subprocess
import sys


def main():

# Retrieving the command and its arguments from the command-line arguments
    command = sys.argv[3]
    args = sys.argv[4:]

# subprocess.run executes the specified command with the provided arguments   
    completed_process = subprocess.run([command, *args], capture_output=True)
    print(completed_process.stdout.decode("utf-8"))

    completed_process = subprocess.Popen([command], *args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(completed_process.stdout.decode("utf-8"))
    print(completed_process.stderr.decode("utf-8"))

if __name__ == "__main__":
    main()
