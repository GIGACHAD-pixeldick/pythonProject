class Project:
    def one(self):
        a = int(input())
        s = 1
        while s ** 2 <= a:
            print(s ** 2)
            s += 1

    def two(self=1, f2=1):
        n = int(input())
        print(self, f2, end=" ")
        while f2 < n:
            print(f2, end=" ")
            self, f2 = f2, self + f2

    def three(self):
        a = int(input())
        b = 1
        counter = 0
        while b != 0:
            b = int(input())
            if b <= a:
                counter += 1
            a = b
        print(counter)
