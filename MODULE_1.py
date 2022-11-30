class Project:
    def first(self):
        a = float(input())
        b = float(input())
        c = float(input())
        d = a + b + c
        print('Результат вычисления суммы трех чисел: ' + str(d))

    def second(self):
        e = float(input())
        e1 = float(input())
        s1 = (e * e1) * 0.5
        print("Результат вычисления площади прямоугольного треугольника: " + str(s1))

    def third(self):
        count = float(input())
        count_minus = count - 1
        count_plus = count + 1
        print("Нынешнее число:",count)
        print("Число до:",count_minus)
        print("Число после:",count_plus)

    def four(self):
        n = int(input())
        k = int(input())
        x = k // n
        y = k - (x * n)
        print("Яблок у студентов:",x)
        print("В корзине:",y)
