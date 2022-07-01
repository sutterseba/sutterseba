import RSA

if __name__ == "__main__":

    n, phi = RSA.initMode()
    e, d = RSA.getKeypair(phi)

    m = 21
    print(f"Message: {m}")

    c = RSA.ENC(m, e, n)
    print(f"Cipher: {c}")

    m = RSA.DEC(c, d, n)
    print(f"Decrypted message: {m}")