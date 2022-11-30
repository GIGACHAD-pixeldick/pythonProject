class Project:
    def one(self):
        while True:
            x = int(input())
            a = x // 10
            b = x % 10
            if x < 10 or x > 100:
                print('Дурак, заново введи')
            else:
                print(b, a, sep=" ")

    def two(self):
        while True:
            x = int(input())
            a = x // 10
            b = x % 10
            if x < 10 or x > 100:
                print('Еблан, заново введи')
            else:
                print(b, a,sep="")

    def three(self):
        import random

        week_days = {
            0: 'воскресенье',
            1: 'понедельник',
            2: 'вторник',
            3: 'среда',
            4: 'четверг',
            5: 'пятница',
            6: 'суббота'
        }
        K = random.randrange(1, 366)
        i = (1 + 3) % 7
        print("1-е января: ", 1)
        print("Номер дня недели: ", i)
        print("День недели:", week_days[i])

    def four(self):
        n = int(input())
        print("Время на электронных часах:",str((n % (60*24))//60),":",str((n % (60*24)) % 60))
