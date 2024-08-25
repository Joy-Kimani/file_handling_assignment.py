# file_handling_assignment.py

def main():
    try:
        # Step 1: Create and write to the file
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("Here is a number: 12\n")
            file.write("This is the third line.\n")
        print("File 'my_file.txt' created and initial content written.")

        # Step 2: Read and display the file contents
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nReading the file after initial write:")
            print(content)

        # Step 3: Append additional content to the file
        with open("my_file.txt", "a") as file:
            file.write("Appending a fourth line.\n")
            file.write("Another number: 123\n")
            file.write("This is the last line.\n")
        print("Additional content appended to 'my_file.txt'.")

        # Step 4: Read and display the updated file contents
        with open("my_file.txt", "r") as file:
            updated_content = file.read()
            print("\nReading the file after appending content:")
            print(updated_content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()
