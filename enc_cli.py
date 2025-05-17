from subs import make_enc_key,comute_dec_key,encrypt_text,decrypt_text

def main():
    enc_key = None
    dec_key = None

    print("enc>")
    while True:
        cmd = input("enc> ").strip().lower()
        match cmd:
            case "exit":
                print("Was nice!\nHope to see you again!")
                break
            case "make enc_key":
                enc_key = make_enc_key()
                dec_key = None
                print("New encryption key created")
            case "make dec_key":
                if not enc_key:
                    print("You must create an encryption key first")
                else:
                    dec_key = comute_dec_key(enc_key)
                    print("Decryption key created")
            case "encrypt":
                if not enc_key:
                    print("You must create an encryption key first!")
                    continue
                print("Please enter your text (end with a carriage return):")
                text = input()
                encrypted = encrypt_text(text,enc_key)
                print("Encoded text:\n" + encrypted)
            case "decrypt":
                if not dec_key:
                    print("You must creat a decryption key first!")
                    continue
                print("Please enter your encrypted text (end with a carriage return):")
                text = input()
                decrypted = decrypt_text(text,dec_key)
                print("Clear text:\n" + decrypted)
            case _:
                print("Unknown command")


if __name__ == "__main__":
      main()  
                                  
        