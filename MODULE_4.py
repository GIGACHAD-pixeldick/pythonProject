class Project:
    def one(self):
        a = int(input())
        if a > 0:
            print("1")
        if a < 0:
            print("-1")
        if a == 0:
            print("0")

    def two(self):
        a = int(input())
        if a in range(100, 1000):
            print("Да")
        else:
            print("Нет")

    def three(self):
        a = int(input())
        if a <= 8:
            if a % 2 == 0 and a != 2 and a != 8:
                print(30)
            if a % 2 > 0:
                print(31)
            elif a == 2:
                print(28)
            elif a == 8:
                print(31)
        if a > 8:
            if a % 2 == 0 and a != 2 and a != 8:
                print(31)
            if a % 2 > 0:
                print(30)

    def four(self):
        a = int(input())
        b = int(input())
        c = int(input())
        if a == b == c:
            print(3)
        elif a == b == c or a == c:
            print(2)
        else:
            print(0)
