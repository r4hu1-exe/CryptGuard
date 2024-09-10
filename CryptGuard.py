import pyfiglet
import pyAesCrypt
from os import stat, remove

def print_banner():
    # Generate and print a figlet banner
    banner = pyfiglet.figlet_format("r4hu1.exe", font="starwars")
    print(banner)

def xor_encrypt_decrypt(path, key):
    try:
        with open(path, 'rb') as fin:
            data = bytearray(fin.read())

        # Apply XOR operation
        for i in range(len(data)):
            data[i] ^= key

        with open(path, 'wb') as fout:
            fout.write(data)
        print("Operation completed successfully.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

def aes_encrypt_decrypt(file_path, password, operation):
    bufferSize = 64 * 1024  # Default buffer size

    if operation == 'encrypt':
        output_path = f"{file_path}.aes"
        with open(file_path, "rb") as fIn:
            with open(output_path, "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
        print("Encryption done. Encrypted file:", output_path)

    elif operation == 'decrypt':
        enc_file_size = stat(file_path).st_size
        output_path = input("Enter the name for the decrypted file (with extension): ")
        try:
            with open(file_path, "rb") as fIn:
                with open(output_path, "wb") as fOut:
                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, enc_file_size)
            print("Decryption done. Decrypted file:", output_path)
        except ValueError:
            print("Error: Decryption failed. Ensure the password is correct and buffer size is appropriate.")

def main():
    print_banner()  # Print the banner at the start
    
    print("****************************************************************************")
    print("\t \t \t MENU")
    print("***************************************************************************")
    print("\t \t 1. Data XOR Encryption and Decryption ")
    print("\t \t 2. Data AES Encryption and Decryption ")
    print("***************************************************************************")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("*************************************")
        print("1. Press 1 for Encryption")
        print("2. Press 2 for Decryption")
        print("*************************************")
        operation = int(input("Enter your choice: "))
        
        if operation in [1, 2]:
            path = input("Enter path of data: ")
            key = int(input("Enter Key for operation: "))
            xor_encrypt_decrypt(path, key)
        else:
            print("Invalid choice. Please enter 1 for Encryption or 2 for Decryption.")

    elif choice == 2:
        print("*************************************")
        print("1. Press 1 for Encryption")
        print("2. Press 2 for Decryption")
        print("*************************************")
        operation = int(input("Enter your choice: "))

        if operation in [1, 2]:
            file_path = input("Enter the file location with extension: ")
            password = input("Enter the password: ")
            op = 'encrypt' if operation == 1 else 'decrypt'
            aes_encrypt_decrypt(file_path, password, op)
        else:
            print("Invalid choice. Please enter 1 for Encryption or 2 for Decryption.")

    else:
        print("Invalid choice. Please enter 1 for XOR or 2 for AES encryption/decryption.")

if __name__ == "__main__":
    main()
