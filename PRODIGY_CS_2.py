from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)

    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))

    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)

    decrypted_pixels = (pixels - key) % 256 
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))

    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    action = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    if action.lower() not in ['e', 'd']:
        print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")
        return

    input_path = input("Enter the path to the input image: ")
    output_path = input("Enter the path to save the output image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if action.lower() == 'e':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
