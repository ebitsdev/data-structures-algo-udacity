import os

def find_files(suffix, path):
    sub_dir = []
    list_files = []
    # Initiate search for files in directories
    # The time complexity here is O(n), n representing the number of files that can be found in a directory
    try:
        for item in os.scandir(path):    
            if item.is_dir():
                sub_dir.append(item.path)
            if item.is_file():
                if item.path.endswith(suffix):
                    list_files.append(item.path)
                    print(list_files)
    except:
        print("There is no such file or directory")
    # The time complexity is O(n) + O(n), n being the number of subdirectories and files respectively
    
    for path in list(sub_dir):
        # Use recursion to search for files in sub directories
        sd, filename = find_files(suffix, path)
        sub_dir.extend(sd)
        list_files.extend(filename)

    return sub_dir, list_files

find_files(".c", "./testdir")
find_files(".c", "./nodir")
find_files(".c", "./newfakeone")