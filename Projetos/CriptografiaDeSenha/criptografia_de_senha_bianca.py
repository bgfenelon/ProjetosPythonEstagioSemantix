import hashlib as hs

class CriptografiaSenha:
    def hash_md5(self,pwd):

        if type(pwd) != str or pwd == None:
            print("Tipo de senha inválido !")
            return 0

        md5 = hs.md5(pwd.encode('utf-8')).hexdigest()
        return md5

    def hash_sha256(self,pwd):

        if type(pwd) != str or pwd == None:
            print("Tipo de senha inválido !")
            return 0

        sha256 = hs.sha256(pwd.encode('utf-8')).hexdigest()
        return sha256


