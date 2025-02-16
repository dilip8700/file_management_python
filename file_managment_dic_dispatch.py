import os
import shutil

def list_files():
    directory = input("enter directory path: ")
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

    menu_options = {
        "1": list_files,
        "2": rename_file,
        "3": delete_path
    }



    while True:
            print("\nFile Management System")
            print("1. List Files")
            print("2. Rename File")
            print("3. Delete File/Directory")
            print("4. Create Directory")
            print("5. Exit")

            choice = input("Enter your choice: ")

            menu_options.get(choice)()
            
           
main()
