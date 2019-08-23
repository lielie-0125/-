import os

file_path = os.path.dirname(__file__)

file_names = os.listdir(file_path)

for file_name in file_names:
    if os.path.isdir(file_name):
        continue
    else:
        if file_name.endswith(".下载"):
            new_file_name = file_name[:-3]
            os.rename(os.path.join(file_path, file_name), os.path.join(file_path, new_file_name))
