import hashlib as hs


def hash_md5(pwd):

    if type(pwd) != str:
        print("Tipo de senha inválido !")
        return 0

    md5 = hs.md5(pwd.encode('utf-8')).hexdigest()
    return md5


def hash_sha256(pwd):

    if type(pwd) != str:
        print("Tipo de senha inválido !")
        return 0

    sha256 = hs.sha256(pwd.encode('utf-8')).hexdigest()
    return sha256


if __name__ == "__main__":

    x = hash_md5('bianca')
    z = hash_sha256('bianca')
    print(x)
    print(z)
