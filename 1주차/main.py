import hashlib

def AutoForensic():
    def hash(self):
        pass
    pass

def Filehashes():
    m1 = hashlib.md5()
    file1 = open("C:\\Users\\yang\\Desktop\\포렌식\\프로그래밍\\1주차\\file1.txt", "br")
    file1_1 = file1.read()
    m2 = hashlib.md5()
    file2 = open("C:\\Users\\yang\\Desktop\\포렌식\\프로그래밍\\1주차\\file2.txt", "br")
    file2_1 = file2.read()

    print("file1 : ", end='')
    m1.update(file1_1)
    m1.digest()
    print(m1.hexdigest())

    print("file2 : ", end='')
    m2.update(file2_1)
    m2.digest()
    print(m2.hexdigest())

def main():
    Filehashes()

if __name__ == "__main__":
    main()
