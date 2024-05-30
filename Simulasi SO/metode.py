#***************************************
# Filename : Metode pada OS
# Programmer : 
# - Muhammad Rifky Afandi
# - Nabilla Assyfa Ramadhani
# - Revana Faliha Salma
# Date : 2024-05-30
#***************************************

# 1. Mkdir : Untuk membuat direktori  
# 2. Mkfile : Untuk membuat File
# 3. Cat : Menampilkan isi pada File
# 4. delete : Menghapus direktori atau file
# 5. ls : menampilkan struktur File
# 6. cd : mengganti path direktori pada PyOS
# 7. mv : mengganti penamaan pada file, atau memindahkan file


import os
import shutil

def mkdir(path):
    try:
        os.makedirs(path)
        print(f'Direktori {path} sukses dibuat')
    except FileExistsError:
        print(f'Direktori {path} sudah tersedia')
    except Exception as e:
        print(f'Error saat membuat direktori {path}: {e}')

def del_file(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f'Menghapus direktori {path} sukses')
        elif os.path.isfile(path):
            os.remove(path)
            print(f'Menghapus File {path} sukses')
        else:
            print(f'{path} does not exist')
    except Exception as e:
        print(f'Error {path}: {e}')

def cd(path):
    try:
        if path == "..":
            os.chdir(os.path.dirname(os.getcwd()))
        else:
            os.chdir(path)
        print(f'Direktori berubah menjadi {os.getcwd()}')
    except FileNotFoundError:
        print(f'Direktori {path} tidak ditemukan')
    except Exception as e:
        print(f'Error changing Direktori to {path}: {e}')

def mkfile(filename):
    try:
        with open(filename, 'w') as f:
            pass
        print(f'File {filename} sukses dibuat')
    except Exception as e:
        print(f'Error creating file {filename}: {e}')

def ls():
    try:
        files = os.listdir(os.getcwd())
        print("Isi direktori anda:")
        for file in files:
            print(file)
    except Exception as e:
        print(f'Error : {e}')

def cat(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f'File {filename} tidak ditemukan')
    except Exception as e:
        print(f'Error saat membaca file {filename}: {e}')

def mv(src, dest):
    try:
        shutil.move(src, dest)
        print(f'{src} diganti {dest}')
    except FileNotFoundError:
        print(f'File atau Direktori {src} tidak ditemukan')
    except Exception as e:
        print(f'Error moving {src} to {dest}: {e}')
