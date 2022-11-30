class Project:
    def one(self):
        lst = list(map(int, input().split()))
        i = 0
        for i in range(len(lst)):
            if lst[i] % 2 == 0:
                pass
            else:
                print(lst[i], end=' ')

    def two(self):
        lst = list(map(int, input().split()))
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:
                print(lst[i], end=' ')

    def three(self):
        lst = list(map(int, input().split()))
        e = set()
        for n in lst:
            if n in e:
                print('ДА')
            else:
                print('НЕТ')
                e.add(n)
