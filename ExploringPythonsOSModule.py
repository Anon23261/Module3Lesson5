import os

# Task 1: Directory Inspector
def list_directory_contents(path):
    # Task: List all files and subdirectories in the specified directory
    try:
        with os.scandir(path) as entries:
            print(f"Contents of '{path}':")
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Task: Prompt user for the directory path to inspect
    user_path = input("Enter the directory path to inspect: ")
    list_directory_contents(user_path)

