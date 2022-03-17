"""Module with collections
"""
import random, typing
import rapidjson as rjson

# deprecated: random.shuffle already exists
# def shuffle(collection: typing.Iterable, /) -> typing.Iterable:
#     result = []
#     copied = collection.copy()
#     while copied:
#         selected = random.chioce(copied)
#         copied.remove(selected)
#         result.append(selected)
#     return result

def merge(collection: typing.Iterable, *args: typing.Iterable) -> list:
    """Merges an iterable collection

    Args:
        collection (typing.Iterable): Base collection
        *args (typing.Iterable): Another collections what appends to base collection

    Returns:
        list: merged collection (list)
    """
    collection = list(collection)
    for coll in args:
        [collection.append(i) for i in coll]
    return collection

class DinfQueue():
    """DinfQueue - Distorted Infinite Queue
    """
    def __init__(self, *args, collection: list = []):
        """Initialize DinfQueue object

        Args:
            collection (list, optional): Collection on which the class is based. Incompatible with *args. Defaults to [].
            *args (typing.Any): Objects what will be appended to base collection. Incompatible with the 'collection' argument

        Raises:
            AttributeError: when *args and 'collection' provides
        """
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
        """Appends object to the end of collection.

        Args:
            obj (object): Object to append
        """
        self.collection.append(obj)
    def shuffle(self):
        """Shuffles collection and replaces that.

        Returns:
            DinfQueue: this object with shuffled collection
        """
        self.collection = self.temp_shuffle()
        return self
    def temp_shuffle(self):
        """Temporary shuffles the collection.

        Returns:
            list(typing.Any): Shuffled collection
        """
        return random.shuffle(self.collection.copy())
    # def next(self):
    # 	try:
    # 		self.index += 1
    # 		return self.collection[self.index-1]
    # 	except IndexError:
    # 		return None
    def reset(self):
        """Resets the index
        """
        self.index = 0
    def clear(self):
        """Clears the collection and index.
        """
        self.collection = []
        self.index = 0
    def upcoming(self):
        """Returns upcoming objects.

        Returns:
            list(typing.Any): Upcoming objects
        """
        return self.collection[self.index+1:]
    def now(self):
        """Returns the value of the collection whose number matches the current index.

        Returns:
            typing.Any: Current object by index
        """
        return self.collection[self.index]

class Line:
    """Line - simple string-like line
    """
    # i think this is an collection
    def __init__(self, sep1: str, sep2: str, length = 10) -> None:
        """Initialize Line object.

        Args:
            sep1 (str): First line separator. This represents filled part of line.
            sep2 (str): Second line separator. This represents empty part of line.
            length (int, optional): Maximum length of the line. Defaults to 10.
        """
        self.sep1 = sep1
        self.sep2 = sep2
        self.__length = 0
        self.__maxlength = length
    def expand(self, value: int):
        """Changes current max line length.

        Args:
            value (int): Which number should the line be changed.
        """
        self._Line__maxlength = value
    def expand(self, value: int):
        """Sets current line length.

        Args:
            value (int): Which number should the line be set to.
        """
        self._Line__length = value
    def increment(self, value: int):
        """Increments length of line.

        Args:
            value (int): How much should the line length be incremented.
        """
        self._Line__length += value
    @property
    def get(self) -> str:
        """Get current view of line.

        Returns:
            str: Current line view.
        """
        a1 = ''
        a2 = ''
        for i in range(self._Line__length):
            a1+=self.sep1
        for i in range(self.__maxlength-self._Line__length):
            a2+=self.sep2
        return a1+a2

class JLJS():
    """JSON object like "objects" in JS"""
    def __init__(self, based_dict: dict = {}, **kwargs) -> None:
        self.JSON = based_dict
        if kwargs:
            for kw, kv in kwargs:
                self.JSON[kw] = kv
    def __getattr__(self, attr):
        return self.JSON.get(attr)
    def __getitem__(self, attr):
        return self.__getattr__(attr)
    def __setattr__(self, name: str, value: typing.Any) -> None:
        self.JSON.__setattr__(name, value)
    def __setitem__(self, name: str, value: typing.Any) -> None:
        self.__setattr__(name, value)
    def __repr__(self):
        return f"<JLJS keys={self.JSON.keys()}>"
    def __str__(self):
        return rjson.dumps(self.JSON, indent=4, ensure_ascii=False)
    def stringify(self):
        return self.__str__()