class Project:
    def one(self):
        n = int(input())
        for a in range(n):
            lst = input()
            my_dict = {i: lst.count(i) for i in lst}
            print(my_dict)

    def two(self):
        n = int(input())
        dict1 = {}
        for i in range(1, n + 1):
            text = input(f'{i}').split(" - ")
            dict1[text[0]] = text[1]
            dict1[text[1]] = text[0]

        while True:
            key = input("\n")
            if key in dict1:
                print(dict1[key])
            else:
                print("Такого слова нет")
            break

    def three(self):
        n1 = int(input())
        dict1 = {}
        for i in range(n1):
            lst = [str(s) for s in input().split(" ")]
            dict1[lst[0]] = list(lst[1:])
        n2 = int(input())
        for i in range(n2):
            lst1 = [str(s) for s in input().split(" ")]
            testlst = dict1[lst1[1]]
            if testlst.count("R") != 0:
                testlst.remove("R")
                testlst.append("read")
            if testlst.count("W") != 0:
                testlst.remove("W")
                testlst.append("write")
            if testlst.count("X") != 0:
                testlst.remove("X")
                testlst.append("execute")
            if testlst.count(lst1[0]) != 0:
                print("OK")
            else:
                print("Denied")

    def four(self):
        n1 = int(input())
        dict1 = {}
        for i in range(n1):
            lst = [str(s) for s in input().split(" ")]
            for j in lst:
                try:
                    dict1[j] = dict1[j] + 1
                except:
                    dict1[j] = 1
        for k,w in sorted(dict1.items()):
            print(k,w)

