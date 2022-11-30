class Project:
    def one(self):
        s = input()
        a = s.find("f")
        b = s.rfind("f")
        if a == -1:
            pass
        elif a == b:
            print(a)
        else:
            print(a,b)

    def two(self):
        a = input()
        print(a.replace("1","one"))

    def three(self):
        a = input()
        print(a.replace("@",""))


