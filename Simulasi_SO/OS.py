#***************************************
# Filename : Tampilan pada OS
# Programmer : 
# - Muhammad Rifky Afandi
# - Nabilla Assyfa Ramadhani
# - Revana Faliha Salma
# Date : 2024-05-31
#***************************************

import os
from metode import *

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
        dir = path_parts[-2: ]
        if 'FileSystems' in dir:
            folder = dir [-1: ]
            return f"PySO/{'/'.join(folder)}"
        else:
            return f"PySO/{'/'.join(dir)}"


def perkenalan () :
    os.system('cls')
    print ("SISTEM OPERASI ILMU KOMPUTER C2")
    print ("Dosen Pengampu : Dr. Rasim, S.T., M.T.")
    print ("_________________________________________")
    print ("!   NIM     !           Nama            !")
    print ("!-----------!---------------------------!")
    print ("!  2202346  ! Muhammad Rifky Afandi     !")
    print ("!  2205297  ! Nabilla Assyfa Ramadhani  !")
    print ("!  2202869  ! Revana Faliha Salma       !")
    print ("!___________!___________________________!")
    print ()
    print ()
    input ("Ketuk 'ENTER' untuk melanjutkan ^_^\n")
    
def pyso ():
    os.system('cls')
    print("Welcome to")
    print("         _____")
    print("        /     \ ")
    print("       /   __  \__    __ _____________ ")
    print("      /        /  /__/  /  ___/       \ ")
    print("     /  ._____/_____   /\  \ /   ___   \ ")
    print("    /   /     _____/  /__\  \\\         / ")
    print("   /___/     /_______/______/ \_______/ version 1.1.0 ")
    print ()
    print ()
    cek = 1 # untuk tanda looping
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
        elif cmd == 'ex':
            cd("..")
        elif cmd == 'nano' and len(args) == 1:
            nano(args[0])
        elif cmd == 'exit':
            print('PySO .... Exiting :)')
            cek = 0
        else:
            print('Perintah tidak ditemukan, mohon masukan perintah sesuai')
