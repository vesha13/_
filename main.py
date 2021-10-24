# используется для сортировки
from operator import itemgetter


class Op:
    """Оператор"""

    def __init__(self, id, op_name, memory, ln_id):
        self.id = id
        self.op_name = op_name
        self.memory = memory
        self.ln_id = ln_id


class Lng:
    """Язык программированя"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class OpLng:
    """
    Операторы языков программирования
    """

    def __init__(self, ln_id, op_id):
        self.ln_id = ln_id
        self.op_id = op_id


# Языки програмиирования
lngs = [
    Lng(1, 'Python'),
    Lng(2, 'С'),
    Lng(3, 'Java'),
    Lng(4, 'C++'),
]

# Операторы
ops = [
    Op(1, 'Сложениее', 4, 1),
    Op(2, 'Умножение', 4, 2),
    Op(3, 'Сравнение', 2, 3),
    Op(4, 'Вызов функции', 8, 3),

]


# Языки и операторы, для связи многие-ко-многим
ln_op = [
    OpLng(1, 1),
    OpLng(2, 2),
    OpLng(3, 3),
    OpLng(3, 4),
    OpLng(1, 2),
    OpLng(1, 4),
    OpLng(2, 1),
    OpLng(2, 3),
    OpLng(3, 1),
    OpLng(3, 2),
    OpLng(1, 4),
    OpLng(4, 4),

]

def main():
    """Основная функция"""
    one_to_many = [(op.op_name, op.memory, ln.name)
                   for ln in lngs
                   for op in ops
                   if op.ln_id == ln.id]

    many_to_many_temp = [(ln.name, lop.ln_id, lop.op_id)
                         for ln in lngs
                         for lop in ln_op
                         if ln.id == lop.ln_id]
    many_to_many = [(op.op_name, op.memory, language)
                    for language, ln_id, op_id in many_to_many_temp
                    for op in ops if op.id == op_id]

    print('Задание В1')
    task1 = []
    for op_name, memory, name in one_to_many:
        if name[0] == "J":
            task1.append((name, op_name))
    print(task1)

    print('\nЗадание В2')
    mas2 = []
    for ln in lngs:
        op_lns = list(filter(lambda i: i[2] == ln.name, one_to_many))
        if len(op_lns) > 0:
            ln_memory = [memory for _, memory, _ in op_lns]
            Memor = min(ln_memory)
            mas2.append((ln.name, Memor))
    task2 = sorted(mas2, key=itemgetter(1))
    print(task2)

    print('\nЗадание В3')
    mas3 = []
    for op_name, memory, name in many_to_many:
        mas3.append((op_name, name))

    task3 = list(sorted(mas3, key=itemgetter(0)))
    print(task3)


if __name__ == '__main__':
    main()

