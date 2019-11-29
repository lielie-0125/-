import pathlib

file_path = pathlib.Path.cwd()

for file_object in file_path.iterdir():
    if file_object.is_dir():
        continue
    elif file_object.is_file():
        if file_object.suffix == ".下载":
            new_file_name = file_object.name[:-3]
            file_object.rename(new_file_name)
