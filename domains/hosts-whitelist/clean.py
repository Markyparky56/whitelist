import sys

def clean_line(line):
    # Remove '127.0.0.1' if it appears at the start of the line
    if line.startswith('127.0.0.1'):
        line = line[len('127.0.0.1'):]
    
    # Strip any leading whitespace
    line = line.lstrip()
    
    return line

def process_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    cleaned_lines = [clean_line(line) for line in lines]
    
    with open(input_file, 'w') as file:
        file.writelines(cleaned_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
    print(f"Processed file '{input_file}' successfully.")
    