from itertools import chain


nested_list = [['a', 'b', 'c'],
	           ['d', 'e', 'f', 'h', False],
	           [1, 2, None],]

class Iterator:
    def __init__(self, lists):
        self.lists = lists

    def __iter__(self):
        self.lists_iter = iter(self.lists)
        self.listed_in = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.listed_in) == self.cursor:
            self.listed_in = None
            self.cursor = 0
            while not self.listed_in:
                self.listed_in = next(self.lists_iter)
        return self.listed_in[self.cursor]



def generator(lists):
     for list1 in lists:
         for item in list1:
             yield item



class Iterator2:
    def __init__(self, lists):
        self.lists = lists

    def __iter__(self):
        self.iterators = []
        self.iterator = iter(self.lists)
        return self

    def __next__(self):
        while True:
            try:
                self.element = next(self.iterator)
            except StopIteration:
                if not self.iterators:
                    raise StopIteration
                else:
                    self.iterator = self.iterators.pop()
                    continue
            if isinstance(self.element, list):
                self.iterators.append(self.iterator)
                self.iterator = iter(self.element)
            else:
                return self.element



def generator2(multi_list):
    for item in multi_list:
        if isinstance(item, list):
            for sub_item in generator2(item):
                yield sub_item
        else:
            yield item

a = '0'
while a != 'x':
	a = input('''Введите решение какой задачи нужно вывести: 1, 2, 3 или 4
Или введите "x" для прекращения работы
''')

	if a == '1':
		for item in Iterator(nested_list):
		    print(item)
	elif a == '2':
		for item in generator(nested_list):
		     print(item)
	elif a == '3':
		for item in Iterator2(nested_list):
		    print(item)
	elif a == '4':
		for item in generator2(nested_list):
		    print(item)
