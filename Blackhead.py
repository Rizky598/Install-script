import os
import time
import sys

# Warna
R = '\033[91m'  # Red
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
C = '\033[96m'  # Cyan
W = '\033[0m'   # White

# Banner
def banner():
    os.system('clear')
    print(f"""{C}
██████╗ ██╗██╗  ██╗██╗  ██╗██╗   ██╗
██╔══██╗██║╚██╗██╔╝╚██╗██╔╝╚██╗ ██╔╝
██████╔╝██║ ╚███╔╝  ╚███╔╝  ╚████╔╝ 
██╔═══╝ ██║ ██╔██╗  ██╔██╗   ╚██╔╝  
██║     ██║██╔╝╚██╗██╔╝╚██╗   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
         Rizky.0_o
{W}""")

# Loading kecil
def loading(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Play Musik
def play_music():
    os.system("ssstik.io_1745714987228.mp3")

# Login Password
def login():
    banner()
    password = "Rizky.0_o"
    inp = input(f"{Y}Masukkan Password: {W}")
    if inp == password:
        print(f"{G}Password Benar! Selamat datang...{W}")
        time.sleep(1)
    else:
        print(f"{R}Password Salah! Keluar...{W}")
        sys.exit()

# Menu
def menu():
    banner()
    print(f"""{C}
╔══════════════════════════════════════════╗
║               MENU PILIHAN                ║
╠══════════════════════════════════════════╣
║ [1] Install Script dari GitHub            ║
║ [2] Update & Upgrade Termux               ║
║ [3] Install Package Tambahan              ║
║ [4] Curhat Sakit Hati (Tulisan Jalan)     ║
║ [5] Keluar                                ║
╚══════════════════════════════════════════╝
{W}""")

# Fungsi-fungsi
def install_script():
    print(f"{Y}Memulai musik latar...{W}")
    play_music()
    time.sleep(2)  # tunggu sebentar biar musik mulai
    url = input(f"{Y}Masukkan Link GitHub script: {W}")
    os.system(f"git clone {url}")
    print(f"{G}Selesai Clone!{W}")
    time.sleep(1)

def update_upgrade():
    os.system("apt update && apt upgrade -y")
    print(f"{G}Selesai Update & Upgrade!{W}")
    time.sleep(1)

def install_package():
    packages = ["python", "git clone ", "curl", "wget", "nano"]
    for package in packages:
        print(f"{C}Menginstall {package}...{W}")
        os.system(f"pkg install {package} -y")
    print(f"{G}Selesai install semua package!{W}")
    time.sleep(1)

def curhat_sakit_hati():
    text = """
    Aku sudah sayang, 
    tapi dia malah pergi.
    Tinggalin luka sedalam jurang.
    Haruskah aku bertahan, 
    atau relakan dia bersama yang lain...
    """
    for line in text.strip().split("\n"):
        loading(f"{R}{line.strip()}{W}")
        time.sleep(0.7)

# Main
def main():
    login()
    while True:
        menu()
        pilihan = input(f"{Y}Pilih menu (1-5): {W}")
        if pilihan == "1":
            install_script()
        elif pilihan == "2":
            update_upgrade()
        elif pilihan == "3":
            install_package()
        elif pilihan == "4":
            curhat_sakit_hati()
        elif pilihan == "5":
            print(f"{G}Keluar... Sampai jumpa, Rizky!{W}")
            break
        else:
            print(f"{R}Pilihan salah!{W}")
        input(f"\n{C}Tekan Enter untuk kembali ke menu...{W}")

if __name__ == "__main__":
    main()
