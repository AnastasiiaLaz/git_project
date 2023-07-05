class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


    def add(self, num):
        self.num = num
        self.value += self.num
        return self.value

    def subtract(self, second_num):
        self.second_num = second_num
        self.value -= self.second_num
        return self.value


# Пример использования, не влияет ни на что, можно удалить.

x = Number(7)
(x.add(3))
(x.subtract(10))
(x.get())

# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())