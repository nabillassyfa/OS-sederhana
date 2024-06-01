#***************************************
# Filename : Main pada PySO
# Programmer : 
# - Muhammad Rifky Afandi
# - Nabilla Assyfa Ramadhani
# - Revana Faliha Salma
# Date : 2024-05-30
#***************************************

from metode import *    # mengambil semua file yang ada pada metode.py
from OS import *

print("Simulasi OS")
initialize_file_system()

cek = 1  # untuk tanda looping
while cek == 1:

    prompt_path = get_relative_path()
    command = input(f'{prompt_path} $~> ').strip().split()
    if len(command) == 0:
        continue
    cmd = command[0].lower()
    args = command[1:]

    if cmd == 'mkdir' and len(args) == 1:
        mkdir(args[0])
    elif cmd == 'del' and len(args) == 1:
        del_file(args[0])
    elif cmd == 'cd' and len(args) == 1:
        cd(args[0])
    elif cmd == 'ls':
        ls()
    elif cmd == 'mkfile' and len(args) == 1:
        mkfile(args[0])
    elif cmd == 'cat' and len(args) == 1:
        cat(args[0])
    elif cmd == 'mv' and len(args) == 2:
        mv(args[0], args[1])
    elif cmd == 'pwd':
        pwd()
    elif cmd == 'cp' and len(args) == 2:
        cp(args[0], args[1])
    elif cmd == 'clear':
        clear()
    elif cmd == 'nano' and len(args) == 1:
        nano(args[0])
    elif cmd == 'ex':
        cd("..")
    elif cmd == 'exit':
        print('PySO .... Exiting :)')
        cek = 0
    else:
        print('Perintah tidak ditemukan, mohon masukan perintah sesuai')