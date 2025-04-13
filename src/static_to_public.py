import os
import shutil

def static_to_public(src, dest):

    if os.path.exists(dest):
        shutil.rmtree(dest)

    if os.path.isfile(src):
        parent_dir = os.path.dirname(dest)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        shutil.copy(src, dest)
        return 
    
    if os.path.exists(src):
        if not os.path.exists(dest):
            os.makedirs(dest, exist_ok=True)

        ls = os.listdir(src)

        for item in ls:
            src_path = os.path.join(src, item)
            file_dest = os.path.join(dest, item)
            if not os.path.isfile(src_path):
                if not os.path.exists(file_dest):
                    os.makedirs(file_dest, exist_ok=True)
                static_to_public(src_path, file_dest)
            else:
                shutil.copy(src_path, file_dest)
    else:
        print(f"Source does not exist: {src}")