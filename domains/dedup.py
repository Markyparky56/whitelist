import sys

def remove_duplicates(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Use a set to store unique lines (removes duplicates automatically)
    unique_lines = set(lines)

    with open(input_file, 'w') as file:
        file.writelines(unique_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    remove_duplicates(input_file)
    print(f"Removed duplicates from file '{input_file}' successfully.")
    