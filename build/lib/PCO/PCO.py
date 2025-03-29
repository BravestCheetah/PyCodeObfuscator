import argparse
import os

def process_file(file_path, verbose=False, count_lines=False, count_words=False):
    """Processes the file based on given flags."""
    file_path = os.path.join(os.getcwd(), file_path)

    if not os.path.isfile(file_path):
        print("Error: File not found!")
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    if verbose:
        print(f"Processing file: {file_path}")

    if count_lines:
        print(f"Line count: {len(content)}")

    if count_words:
        word_count = sum(len(line.split()) for line in content)
        print(f"Word count: {word_count}")

def main():
    parser = argparse.ArgumentParser(description="Process a file with given flags.")
    parser.add_argument("file", type=str, help="Path to the file (relative to current working directory)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--lines", "-l", action="store_true", help="Count lines in the file")
    parser.add_argument("--words", "-w", action="store_true", help="Count words in the file")

    args = parser.parse_args()
    process_file(args.file, args.verbose, args.lines, args.words)

if __name__ == "__main__":
    main()
