# task1.py

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("Reading file content:")
            for i, line in enumerate(file, start=1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    read_file("sample.txt")

-- output --

Error: The file 'sample.txt' was not found.

