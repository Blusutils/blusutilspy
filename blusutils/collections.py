"""Module with collections
"""
import random, typing
import rapidjson as rjson
from .errors import *

def deep_merge(source: dict, destination) -> dict:
    """Deep merge for dictionaries

    Args:
        source (dict): Dict to merge
        destination (Any): hm...

    Returns:
        dict: hm...
    """
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            deep_merge(value, node)
        else:
            destination[key] = value
    return destination

def difflist(list1: list, list2: list) -> list:
    """Showing difference between two lists

    Args:
        list1 (list): First list to check difference
        list2 (list): Second list to check difference

    Returns:
        list: Difference between list1 and list2
    """
    return list(set(list1).symmetric_difference(set(list2)))

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
        self.collection: list = []
        self.collection.extend(args)
        self.collection.extend(collection)
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
        for i in self.collection[self.index:]:
            yield i
        #return iter(self.collection)
    def next(self):
        try:
            self.index += 1
            return self.collection[self.index]
        except IndexError:
            self.index -= 1
            raise QueueEnded(f'the queue was ended. Last index: {self.index}')
    def previous(self):
        try:
            self.index -= 1
            return self.collection[self.index]
        except IndexError:
            self.index += 1
            raise QueueAtStart('the queue reached start of self')
    def append(self, obj: object):
        """Appends object to the end of collection.

        Args:
            obj (object): Object to append
        """
        self.collection.append(obj)
    def extend(self, obj: typing.Iterable):
        """Extends collection from iterable.

        Args:
            obj (object): Object to append
        """
        self.collection.extend(obj)
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
    def setlength(self, value: int):
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


# Bug: getattr goes to recursion
# class JLJS():
#     """JSON object like "objects" in JS"""
#     def __init__(self, based_dict: dict = {}, **kwargs) -> None:
#         self._JSON = based_dict
#         if kwargs:
#             for kw, kv in kwargs:
#                 self._JSON[kw] = kv
#     def __getattr__(self, attr):
#         return self._JSON.get(attr, None)
#     def __getitem__(self, attr):
#         return self._JSON.get(attr, None)
#     def __setattr__(self, name: str, value: typing.Any) -> None:
#         self._JSON.__setattr__(name, value)
#     def __setitem__(self, name: str, value: typing.Any) -> None:
#         self.__setattr__(name, value)
#     def __repr__(self):
#         return f"<JLJS keys={self._JSON.keys()}>"
#     def __str__(self):
#         return rjson.dumps(self._JSON, indent=4, ensure_ascii=False)
#     def stringify(self):
#         return self.__str__()