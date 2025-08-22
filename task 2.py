

def write_and_append(filename):
   
    text = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(text + "\n")
    print(f"Data successfully written to {filename}.")

   
    more_text = input("Enter additional text to append: ")
    with open(filename, "a") as file:
        file.write(more_text + "\n")
    print("Data successfully appended.")

   
    print(f"\nFinal content of {filename}:")
    with open(filename, "r") as file:
        print(file.read())

if __name__ == "__main__":
    write_and_append("output.txt")

-- Output --
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
