import os
import shutil

def list_files(directory):
    files = os.listdir(directory)
    if not files:
        print("No files found in the directory")
    else:  
        for file in files:
            print(file)
    
def rename_file(directory, old_name, new_name):
    old_path = os.path.join(directory,old_name)
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)
    print("File Renamed Successfully!")

def delete_path(directory,name):
    path = os.path.join(directory, name)
    if os.path.isfile(path):
        os.remove(path)
        print("File delete Successfully!")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print("Directory deleted successfully!")
    else:
        print("The Specified path does not exist.")

def create_directory(directory, folder_name):
    path = os.path.join(directory, folder_name)
    os.makedirs(path, exist_ok=True)
    print("Directory created Successfully")
    

def main():
        print("\nFile Management System")
        print("1. List Files")
        print("2. Rename File")
        print("3. Delete File/Directory")
        print("4. Create Directory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            directory = input("enter directory path: ")
            list_files(directory)
        elif choice == "2":
            directory = input("enter directory path: ")
            old_name = input("enter old file name: ")
            new_name = input("enter new file name: ")
            rename_file(directory,old_name,new_name)
        elif choice == "3":
            directory = input("enter directory path: ")
            name = input("Enter file or directory name to delete: ")
            delete_path(directory, name)
        elif choice == "4":
            directory = input("enter directory path: ")
            folder_name = input("enter new folder name: ")
            create_directory(directory, folder_name)

main()
