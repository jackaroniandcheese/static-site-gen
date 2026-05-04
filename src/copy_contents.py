import os
import os.path as p
import shutil

def copy_contents(source, destination):
    if p.exists(destination):
        print(f"Deleting {destination}")
        shutil.rmtree(destination)
    print(f"Creating {destination}")
    os.mkdir(destination)
    copy_contents_helper(source, destination)

def copy_contents_helper(source, destination):
    contents = os.listdir(source)
    for item in contents:
        full_source = p.join(source, item)
        full_destination = p.join(destination, item)
        if p.isfile(full_source):
            print(f"Copying {full_source} to {full_destination}")
            shutil.copy(full_source, full_destination)
        else:
            print(f"{full_source} not a file, making dir at {full_destination}")
            os.mkdir(full_destination)
            copy_contents_helper(full_source, full_destination)
