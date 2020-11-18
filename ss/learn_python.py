def main(name):
    print(f'This is the main method, {name}')
    a = 3
    b = 4
    print(a+b)
    a = "sample"
    print(a)
    my_list = [1,2,3,4]
    print(my_list[-1])
    print(my_list[-2])
    str1 = "sam'ple"
    str2 = 'sam"ple'
    print(str1+str2)
    if (3 > 4) :
        print("within if loop")
    print("outside if loop")

    for i in range(5):
        print("value of i ",i)
        print(" value of i >>> {}".format(i))

    my_list2 = [1,2,3,4,5,6]

    for j in my_list2:
        print(" value of j >>> {}".format(j))

    var2 = calcualateSum(5,6)
    print(var2)

    var3,var4= calcualateSumAndMult(10,20)
    print(var3)
    print(var4)

    with open("my_file_1.txt","w") as f:
        f.write("sample content 1")

    with open("my_file_1.txt", "a") as f:
        f.write("more content")

    with open("my_file_1.txt", "w") as f:
        f.write("new content")

def calcualateSum(a,b):
    return a+b

def calcualateSumAndMult(a,b):
    return a+b,a*b

if __name__ == '__main__':
    print("beginning execution")
    main('PyCharm')
