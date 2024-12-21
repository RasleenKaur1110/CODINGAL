import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

def write_file(file_path):
    content = input("Enter the content to write to the file: ")
    with open(file_path, 'w') as file:
        file.write(content)
    print("Content written successfully.")

def append_file(file_path):
    content = input("Enter the content to append to the file: ")
    with open(file_path, 'a') as file:
        file.write(content)
    print("Content appended successfully.")

def main():
    print("File Operations:")
    print("1. Read file")
    print("2. Write file")
    print("3. Append to file")
    print("4. Exit")
    
    file_path = input("Enter the file path: ")
    
    while True:
        try:
            choice = int(input("\nChoose an operation: "))
            if choice == 1:
                read_file(file_path)
            elif choice == 2:
                write_file(file_path)
            elif choice == 3:
                append_file(file_path)
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a valid operation.")
        except ValueError:
            print("Please enter a numeric choice.")

if __name__ == "__main__":
    main()