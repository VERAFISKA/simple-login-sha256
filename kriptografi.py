import hashlib

# Tempat penyimpanan data user
database = {}

def buat_hash(teks):
    return hashlib.sha256(teks.encode()).hexdigest()

def fungsi_registrasi():
    print("\n[ Registrasi ]")
    username = input("Username baru: ")
    
    if username in database:
        print("Username sudah terdaftar.")
        return
        
    password = input("Password baru: ")
    hash_password = buat_hash(password)
    database[username] = hash_password
    
    print("Hash SHA-256 : " + hash_password)
    print("Status       : Registrasi Berhasil")

def fungsi_login():
    print("\n[ Login ]")
    username = input("Username: ")
    password = input("Password: ")
    
    hash_input = buat_hash(password)
    print("Hash Input    : " + hash_input)
    
    if username in database:
        hash_database = database[username]
        print("Hash Database : " + hash_database)
        
        if hash_database == hash_input:
            print("Status Login  : BERHASIL")
        else:
            print("Status Login  : GAGAL")
    else:
        print("Hash Database : Tidak Ditemukan")
        print("Status Login  : GAGAL")

def menu_utama():
    while True:
        print("\n=== MENU ===")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilihan (1-3): ")
        
        if pilihan == '1':
            fungsi_registrasi()
        elif pilihan == '2':
            fungsi_login()
        elif pilihan == '3':
            print("Program Selesai.")
            break
        else:
            print("Pilihan salah.")

if __name__ == "__main__":
    menu_utama()