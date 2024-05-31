#***************************************
# Filename : Tampilan pada OS
# Programmer : 
# - Muhammad Rifky Afandi
# - Nabilla Assyfa Ramadhani
# - Revana Faliha Salma
# Date : 2024-05-31
#***************************************

import os

# direktori dan file yang dibuat dimasukkan kedalam file systems
ROOT_DIR = "FileSystems"

# inisialisasi file systems
def initialize_file_system():
    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)
    os.chdir(ROOT_DIR)
    
def get_relative_path():
    current_path = os.getcwd()
    relative_path = current_path.replace(os.path.abspath(ROOT_DIR), "")
    path_parts = relative_path.strip(os.sep).split(os.sep)
    path = path_parts[-1:]
    if path == ['FileSystems']:
        return "PySO"
    else:
        return f"PySO/{'/'.join(path)}"