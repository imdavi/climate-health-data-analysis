import os

def create_if_doesnt_exist(directory_path):
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)