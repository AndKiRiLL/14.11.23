# Класс "Снежинки" Snow
'''
class Snow:
    def __init__(self, num):
        self.num = num

    def make_snow(self, el):
        for i in range(self.num // el):
            print('*' * el)
        print('*' * (self.num % el))

    def __add__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError

        # if isinstance(other, int):
        #     res = other
        # else:
        #     res = other.num
        res = other if isinstance(other, int) else other.num
        return Snow(self.num + res)

    def __sub__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        res = other if isinstance(other, int) else other.num
        return Snow(self.num - res)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num * other)

    def __floordiv__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num // other)

    def __truediv__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num // other)


s = Snow(100)
s = s / 2
s.make_snow(10)
'''

# Класс «Снежинка» (SnowFlake)

class SnowFlakes:
    def __init__(self, n):
        self.n = n
        self.m = [["-" for i in range(n)] for j in range(n)]
        for i in range(n):
            self.m[i][i] = "*"
        for i in range(n, 0, -1):
            self.m[i - 1][n - i] = "*"
        for i in range(n):
            self.m[i][n // 2] = "*"
            self.m[n // 2][i] = "*"
        self.k = 0
        self.count = 0
        self.g = 0

    def thaw(self, times, TF=True):
        if TF:
            self.g += times
        for i in range(times):
            self.k = 0
            while self.m[self.k][self.k] != "*":
                self.k += 1
            self.m[self.k] = ["-" for i in range(len(self.m))]
            for j in range(len(self.m)):
                self.m[j][self.k] = "-"
            self.m[- 1 - self.k] = ["-" for i in range(len(self.m))]
            for j in range(len(self.m)):
                self.m[j][- 1 - self.k] = "-"

    def thicken(self, new=False):
        if new:
            self.mainthicken(0)
        else:
            self.mainthicken(1)

    def mainthicken(self, plusorzero):
        self.count += plusorzero
        self.k = 0
        while self.m[self.k][self.k] == "-":
            self.k += 1
        for i in range(self.g - self.k):
            self.m = [["-" for i in range(len(self.m))]] + self.m + [["-" for i in range(len(self.m))]]
            for k in range(len(self.m)):
                self.m[k] = ["-"] + self.m[k] + ["-"]
        self.g = 0
        for i in range(len(self.m)):
            self.m[i][i], self.m[i][len(self.m) // 2], self.m[len(self.m) // 2][i] = "*", "*", "*"
            self.m[len(self.m) // 2][i] = "*"
            self.m[i][- 1 - i] = "*"
        for i in range(len(self.m)):
            if i + self.count < len(self.m):
                self.m[i + self.count][i] = "*"
            self.m[i - self.count][i] = "*"
            self.m[i][len(self.m) // 2 + self.count] = "*"
            self.m[i][len(self.m) // 2 - self.count] = "*"
            self.m[len(self.m) // 2 + self.count][i] = "*"
            self.m[len(self.m) // 2 - self.count][i] = "*"
            if i + self.count < len(self.m):
                self.m[i + self.count][-i - 1] = "*"
            self.m[i - self.count][-i - 1] = "*"

    def freeze(self, kol):
        for i in range(kol):
            self.m = [["-" for i in range(len(self.m))]] + self.m + [["-" for i in range(len(self.m))]]
            for k in range(len(self.m)):
                self.m[k] = ["-"] + self.m[k] + ["-"]
        for i in range(kol):
            self.k = 0
            while self.m[self.k][self.k] != "*":
                self.k += 1
            self.m[self.k - 1][self.k - 1], self.m[- self.k][- self.k] = "*", "*"
            self.m[self.k - 1][- self.k], self.m[- self.k][self.k - 1] = "*", "*"
            self.m[self.k - 1][len(self.m) // 2], self.m[- self.k][len(self.m) // 2] = "*", "*"
            self.m[len(self.m) // 2][self.k - 1], self.m[len(self.m) // 2][- self.k] = "*", "*"
            self.thicken(True)
            self.thaw(self.k - 1, False)

    def show(self):
        for i in self.m:
            print("".join(i))


sf = SnowFlakes(11)

sf.show()
sf.thaw(2)
print()
sf.show()
print()
sf.freeze(1)
sf.show()

# Класс "Robot"
'''
class Robot:
    MAX_X = 100
    MAX_Y = 100


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path_list = [[self.x, self.y]]

    def move(self, let_path):
        self.path_list = [[self.x, self.y]]

        for i in let_path:
            if i == 'N' and self.y < self.MAX_Y:
                self.y += 1
            elif i == 'S' and self.y > 0:
                self.y -= 1
            elif i == 'E' and self.x < self.MAX_X:
                self.x += 1
            elif i == 'W' and self.x > 0:
                self.x -= 1
            self.path_list.append([self.x, self.y])

        print(f'x: {self.x}, y: {self.y}')

    def path(self):
        print('Path:')
        for i in self.path_list:
            print(i)


r = Robot(3, 4)

r.move('NNWWWEESNNN')
r.path()
'''


# Класс «Разговор» (Talking)
'''
class Talking:

    def __init__(self, name):
        self.name = name
        self.answer = True
        self.num_yes = 0
        self.num_no = 0

    def to_answer(self):
        if self.answer == True:
            self.answer = False
            self.num_yes += 1
            return 'moore-moore'

        elif self.answer == False:
            self.answer = True
            self.num_no += 1
            return 'meow-meow'

    def number_yes(self):
        return self.num_yes

    def number_no(self):
        return self.num_no


# # Пример 1
# tk = Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')


# Пример 2
tk = Talking('Pussy')
tk1 = Talking('Barsik')
print(tk.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')
'''
