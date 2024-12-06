def append_to_file(filename):
    with open(filename, 'a') as file:
        new_entry = input("Enter the new entry (e.g., 'Name, Favorite Subject: Subject'): ")
        if new_entry.strip():
            file.write(new_entry + '\n')
            print(f"Entry added to '{filename}'.")
        else:
            print("Invalid entry. Please enter a valid string.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("\nFile Content:")
            content = file.readlines()
            for line in content:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please ensure the file exists.")

def main():
    filename = 'data.txt'
    
    while True:
        print("\nMenu:")
        print("1. Append a new entry to the file")
        print("2. Read and display the file content")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            append_to_file(filename)
        elif choice == '2':
            read_file(filename)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
