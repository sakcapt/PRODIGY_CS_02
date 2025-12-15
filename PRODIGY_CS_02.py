from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)

    # XOR each pixel with the key
    encrypted_arr = arr ^ key

    encrypted_img = Image.fromarray(encrypted_arr)
    encrypted_img.save(output_path)
    print("Image encrypted and saved as:", output_path)


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)

    # XOR again with the same key = decryption
    decrypted_arr = arr ^ key

    decrypted_img = Image.fromarray(decrypted_arr)
    decrypted_img.save(output_path)
    print("Image decrypted and saved as:", output_path)


# ===== MAIN PROGRAM =====
print("=== Image Encryption Tool ===")
mode = input("Choose mode (encrypt/decrypt): ").lower()

input_path = input("Enter input image path: ")
output_path = input("Enter output image name: ")
key = int(input("Enter numeric key (1–255): "))

if mode == "encrypt":
    encrypt_image(input_path, output_path, key)

elif mode == "decrypt":
    decrypt_image(input_path, output_path, key)

else:
    print("Invalid option!")
