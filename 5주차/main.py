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
    hashdb = []
    for i in range(1,11):
        md5 = hashlib.md5()
        gethash = 'C:\\Users\\yang\\Desktop\\포렌식\\프로그래밍\\2주차\\file{0}.txt'.format(i)
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

def MBRtoInt():
    strings = ['002021000CFEFFFF0008000000C09403', '00FEFFFF07FEFFFF00C8940300C09403']
    result_list = [[],[],[],[]]

    for j in range(len(strings)):
        string_list = [strings[j][k]+strings[j][k+1] for k in range(0, len(strings[j])-16, 2)]
        exstring1 = strings[j][-10:-8]+strings[j][-12:-10]+strings[j][-14:-12]+strings[j][-16:-14]
        exstring2 = strings[j][-2:]+strings[j][-4:-2]+strings[j][-6:-4]+strings[j][-8:-6]
        

        for i in string_list:
            result_list[j].append(int(i,16))

        result_list[j].append(int(exstring1,16))
        result_list[j].append(int(exstring2,16))
        if result_list[j][0] == 0:
            print("{0}번째 파티션은 부팅 불가능한 파티션입니다.".format(j+1))
        else :
            print("{0}번째 파티션은 부팅 가능한 파티션입니다.".format(j+1))
        
    print(result_list)

def FileHex():
    startstring = int(input("start : "))
    lenstring = int(input("length : "))
    with open("20230331_ence.001", "rb") as f:
        #print(f.read()[startstring:startstring+lenstring])
        print(f.read()[:5])
        f.close()

def IntToHex():
    resultmanu = ['00','00','00','00']
    changeint = int(input("number: "))
    manuint = hex(changeint)[2:]
    if len(manuint) % 2 == 0:
        for i in range(int(len(manuint)/2)):
            j = i+1
            if i == 0:
                resultmanu[i] = str(manuint[-j*2:])
            else:
                resultmanu[i] = manuint[-j*2:-j]
        print(' '.join(resultmanu))
    else:
        manuint = '0'+manuint
        for i in range(int(len(manuint)/2)):
            j = i+1
            if i == 0:
                resultmanu[i] = str(manuint[-j*2:])
            else:
                resultmanu[i] = manuint[-j*2:-j]
        print(' '.join(resultmanu))

def gifcarv():
    filename = None
    try:
	bytes = binascii.unhexlify(hex_content)
	filename = 'C:\\Users\\yang\\Documents\\recive\\' + hashlib.md5(bytes).hexdigest() + '.gif'
	f_out = open(filename, 'wb')
	f_out.write(bytes)
	f_out.close()

    except:
	print("Invalid [binascii]")
	return

    if imghdr.what(filename) == None:
	os.remove(filename)
	print("Invalid [imghdr]")
    else:
	print("**** Image Saved ****")
	return True
    

def main():
    '''print("1 : Filehashes()")
    print("2 : appendhash()")
    print("3 : MBRtoInt")
    num = input("num : ")

    if num == 1:
        Filehashes()
    elif num == 2:
        appendhash()
    elif num == 3:
        MBRtoInt()'''

    #Filehashes()
    #appendhash()
    #MBRtoInt()
    #FileHex()
    #IntToHex()
    #gifcarv()


if __name__ == "__main__":
    main()
