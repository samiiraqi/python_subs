import random
import string

#Function to create a random encryption key
def make_enc_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    enc_key = dict(zip(letters , shuffled))
    return enc_key

#Function to compute the decryption key from the encryption key
def comute_dec_key(enc_key):
    dec_key = {v:k for k , v in enc_key.items()}
    return dec_key

#Function to encrypt text using the encryption key
def encrypt_text(text , enc_key):
    encrypted = []
    for char in text.lower():
        if char in enc_key:
            encrypted.append(enc_key[char])
        else:
            encrypted.append(char)
    return "".join(encrypted)

#Function to decrypt tex using the decryption key
def decrypt_text(encrypt_text, dec_key):
    decrypted = []
    for char in encrypt_text:
        if char in dec_key:
            decrypted.append(dec_key[char])
        else:
            decrypted.append(char)
    return "".join(decrypted)

#Function to demonstrate the full process
def test_all():
    print("=== Substitution Cipher Demo ===")
    enc_key = make_enc_key()
    print(f"Encryption Key:\n{enc_key}")

    dec_key = comute_dec_key(enc_key)
    print(f"Decryption Key:\n{dec_key}\n")

    sample_text = "Hello world! This is a test message."
    print(f"Original Text:\n{sample_text}\n")

    encrypted = encrypt_text(sample_text , enc_key)
    print(f"Encrypted Text:\n{encrypted}\n")

    decrypted = decrypt_text(encrypted , dec_key)
    print(f"Decrypted Text:\n{decrypted}\n")

#Run the demonstration
if __name__ == "__main__":
      test_all()            