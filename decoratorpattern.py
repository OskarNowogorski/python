#allows you to create new behaviours to objects
class UndecoratedObject:
    def __init__(self, string):
        self.str = string

    def get_string(self):
        return self.str


class DecoratedObject:
    def __init__(self, obj):
        self.undecorated_object = obj

    def get_string(self):
        return self.undecorated_object.get_string().replace("undecorated", "decorated")

#Create two instances and returns of the methods
undecorated = UndecoratedObject("Hello, I am undecorated")
print(undecorated.get_string())

decorated = DecoratedObject(undecorated)
print(decorated.get_string())