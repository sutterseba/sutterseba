import RSA

def main ():
    n, phi = RSA.init_mode()
    e, d = RSA.get_keypair(phi)

    m = 21
    print(f"Message: {m}")

    c = RSA.encrypt(m, e, n)
    print(f"Cipher: {c}")

    m = RSA.decrypt(c, d, n)
    print(f"Decrypted message: {m}")

if __name__ == "__main__":
    main()