# PyCodeObfuscator

PyCodeObfuscator is a Python-based tool designed to securely obfuscate Python source files. With a focus on simplicity and utility, this script ensures your code is protected while maintaining functionality.

## Features
- Obfuscates Python files to protect sensitive source code.
- Supports verbose output for detailed feedback during the obfuscation process.
- User-friendly interface with clear error handling and concise messaging.

## Installation
You can install PyCodeObfuscator via pip:
```bash
pip install pycodeobfuscator
```
Alternatively, clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/PyCodeObfuscator.git
cd PyCodeObfuscator
```
## Usage
Run the script with the following syntax:
```bash
pycodeobfuscator <file> [-v | --verbose] [-s | --single]
```
or
```bash
PCO <file> [-v | --verbose] [-s | --single]
```
### Arguments
- `<file>`: The path to the Python file you want to obfuscate.
- `-v` or `--verbose`: Enables verbose mode for additional output.
- `-s` or `--single`: Only obfuscates the code once, not as obfuscated but will result in a smaller file

### Example
```bash
pycodeobfuscator script.py --verbose
```
Output:
```
[INFO] Obfuscating, Iteration: 1/20
[INFO] Obfuscating, Iteration: 2/20
[INFO] Obfuscating, Iteration: 3/20
...
[INFO] Obfuscating, Iteration: 20/20
[INFO] Obfuscating...
[INFO] Obfuscated file saved as: script_obf.py
[INFO] File successfully obfuscated! Result Character Lenght: 2216948
```
## How It Works
1. **Input File**: Supply the path to a Python source file.
2. **Obfuscation**: The tool processes and obfuscates the file to make the file less readable.
    Now this part is broken down into peices, first all comments and empty liens are removed. Then the command splits the code into smaller chunks and picks a random function out of a list of encoding functions containing functions such as base64, gzip etc. Then it formats the output of the endoing together with some randomly picked variable names and formats them into python syntax. Lastly it adds a exec() containing the decoding of all the variables.
     After that this process is repeated 20 times to obfuscate it as much as possible (to prevent this repetition use the -s (--single) flag to only obfuscate once.)
4. **Output File**: An obfuscated version of the file is saved in the same directory.

## Requirements
- Python 3.6 or higher
- termcolor library for colored console output

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Thanks to the open-source community for supporting the development of tools like PyCodeObfuscator!
