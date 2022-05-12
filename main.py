nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
nested_list2 = [11, ['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None], 11]
nested_list4 = [11, ['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None, [222, 222, [333, 333, [444, 444]]]], 11]

# задание 1
print('задание 1')


class FlatIterator:
    def __init__(self, lst):
        self.x = -1
        self.lst = lst

    def __iter__(self):
        self.x += 1
        self.y = 0
        return self

    def __next__(self):
        len1 = len(self.lst[self.x])
        if self.y == len1:
            iter(self)
        len2 = len(self.lst)
        if self.x == len2:
            raise StopIteration
        self.y += 1
        return self.lst[self.x][self.y-1]


flat_list = [i for i in FlatIterator(nested_list)]
print(flat_list)
# задание 1

# генератор  задание 2 начало
print('задание 2')


def flat_generator2(lst):
    for x in lst:
        if isinstance(x, list):
            for y in x:
                yield y
        else:
            yield x


flat_list = [i for i in flat_generator2(nested_list2)]
print(flat_list)
# генератор  задание 2 конец

# генератор  задание 4
print('задание 4')


def flat_generator4(lst):
    for x in lst:
        if isinstance(x, list):
            for y in flat_generator4(x):
                yield y
        else:
            yield x


flat_list = [i for i in flat_generator4(nested_list4)]  # nested_list  любой
print(flat_list)
# генератор  задание 4 конец
