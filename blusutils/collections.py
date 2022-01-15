import random, typing

def shuffle(collection: typing.Iterable, /) -> typing.Iterable:
    result = []
    copied = collection.copy()
    while copied:
        selected = random.chioce(copied)
        copied.remove(selected)
        result.append(selected)
    return result

def merge(collection: typing.Iterable, *args: typing.Iterable) -> list:
    collection = list(collection)
    for coll in args:
        [collection.append(i) for i in coll]
    return collection

class DinfQueue():
    def __init__(self, *args, collection: list = []):
        self.collection = []
        if args and not collection:
            self.collection = list(args)
        elif collection and not args:
            self.collection = collection
        elif not collection and not args:
            pass
        else:
            raise AttributeError('args and collection provided')
        self.index = 0
    def __repr__(self):
        return f'DinfQueue({str(self.collection)})'
    def __len__(self):
        return len(self.collection)
    def __reversed__(self):
        return DinfQueue(collection = self.collection[::-1])
    def __contains__(self, item):
        return item in self.collection
    def __getitem__(self, key):
        return self.collection[key] if isinstance(key, int) else None
    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.collection[key] = value
        else:
            raise TypeError(f'key must be {int}, not {type(key)}')
    def __delitem__(self, key):
        del self.collection[key]
    def __iter__(self):
        return iter(self.collection)
    def __next__(self):
        try:
            self.index += 1
            return self.collection[self.index-1]
        except IndexError:
            raise StopIteration
    def __aiter__(self):
        return iter(self.collection)
    def __anext__(self):
        try:
            self.index += 1
            return self.collection[self.index-1]
        except IndexError:
            raise StopAsyncIteration
    def append(self, obj: object):
        self.collection.append(obj)
    def shuffle(self):
        self.collection = self.temp_shuffle()
        return self
    def temp_shuffle(self):
        result = []
        copied = self.collection.copy()
        while copied:
            selected = random.chioce(copied)
            copied.remove(selected)
            result.append(selected)
        return result
    # def next(self):
    # 	try:
    # 		self.index += 1
    # 		return self.collection[self.index-1]
    # 	except IndexError:
    # 		return None
    def reset(self):
        self.index = 0
    def clear(self):
        self.collection = []
        self.index = 0
    def upcoming(self):
        return self.collection[self.index+1:]
    def now(self):
        return self.collection[self.index]

class Line:
    # i think this is an collection
    def __init__(self, sep1, sep2, length = 10) -> None:
        self.sep1 = sep1
        self.sep2 = sep2
        self.__length = 0
        self.__maxlength = length
    def expand(self, value):
        self._Line__length = value
    def increment(self, value):
        self._Line__length += value
    @property
    def get(self) -> str:
        a1 = ''
        a2 = ''
        for i in range(self._Line__length):
            a1+=self.sep1
        for i in range(self.__maxlength-self._Line__length):
            a2+=self.sep2
        return a1+a2