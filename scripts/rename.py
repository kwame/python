import os

def rename_files(directory):
    if not os.path.exists(directory):
        print(f"El directorio '{directory}' no existe.")
        return
    
    files = os.listdir(directory)

    for filename in files:
        _, ext = os.path.splitext(filename)

        if ext != '.txt':
            new_filename = os.path.join(directory, f"{os.path.splitext(filename)[0]}.txt")

            try:
                os.rename(os.path.join(directory, filename), new_filename)
                print(f"Renombrando '{filename} a '{os.path.basename(new_filename)}'")
            except OSError as e:
                print(f"Error: {e}")

        else:
            print(f"'{filename}' ya tiene extensión .txt")

directory_path = '/home/kwame/Code/python/filesa'

rename_files(directory_path)
