import subprocess
import sys


def main():
    print("Logs from your program will appear here!")
    
# Retrieving the command and its arguments from the command-line arguments
    command = sys.argv[3]
    args = sys.argv[4:]

# subprocess.run executes the specified command with the provided arguments   
    completed_process = subprocess.run([command, *args], capture_output=True)
    print(completed_process.stdout.decode("utf-8"))


if __name__ == "__main__":
    main()
