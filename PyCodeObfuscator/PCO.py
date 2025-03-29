import sys
from termcolor import colored

class File():
    def __init__(self, file):
        self.file = file

    def obfuscate():
        pass

def main():
    error = colored("[ERROR]", "red")
    warning = colored("[WARNING]", "yellow")
    info = colored("[INFO]", "green")
    
    if len(sys.argv) < 2:
        print(error, "Usage: PyCodeObfuscator <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(info, f"Loading file: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        print(info, "File Content Loaded")
    except FileNotFoundError:
        print(error, f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(error, f"An error occurred: {e}")
