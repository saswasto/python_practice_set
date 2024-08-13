import os

def print_directory_contents(path='.'):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path you want to list (default is current directory)
directory_path = '.'

# Print the contents of the directory
print_directory_contents(directory_path)
