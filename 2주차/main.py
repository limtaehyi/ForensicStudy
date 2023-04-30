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

def appendhash():
    for i in range(1,11):
        md5 = hashlib.md5()
        gethash = 'file{0}.txt'.format(i)
        with open(gethash, 'rb') as f:
            while True:
                data = f.read(8192)
                if not data:
                    break
                md5.update(data)
        hashdb.append(md5.hexdigest())
    print(hashdb)
    mint = 0
    want = input("hash : ")
    for index,text in enumerate(hashdb):
        if want == text:
            mint = 1
            print("file{0}.txt".format(index+1))

    if mint == 0:
        print("can't find")

def main():
    Filehashes()

if __name__ == "__main__":
    main()
