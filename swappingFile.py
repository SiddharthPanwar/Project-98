def swapFileData():
    fileName=input("Enter The File Name : ")
    f=open(fileName,"r")
    with open(swap1, 'r') as a:
    data_a = a.read()
    with open(swap2, 'r') as b:
    data_b = b.read()
    with open(swap1, 'w') as a:
    a.write(data_b)
    with open(swap2, 'w') as b:
    b.write(data_a)

swapFileData()