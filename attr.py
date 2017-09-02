#!/usr/bin/python3

class testAttr(object):
    """docstring for testAttr"""
    def __init__(self, name, age):
        super(testAttr, self).__init__()
        self._name = name
        self.age = age
    def get_name(self):
        return self._name
    def set_name(self, name):
        # self._name = name
        self.__dict__['_name'] = name

    name = property(get_name, set_name)

    def __setattr__(self, name, value):
        if name == 'info':
            self._name, self.age = value
        else:
            self.__dict__[name] = value   #动态的给类增加录属性。 __dict__是保存类全部属性的字典

    def __getattr__(self, name):
        if name == 'info':
            return (self.age, self._name)            
        else:
            raise AttributeError

    def show_attr_dict(self):
        """
            show all this class attr.
        """
        print(self.__dict__)        #__dict__是保存类全部属性的字典



tom = testAttr('tom', 22)

print(tom)

tom.info = ('tom2', 23)
print(tom.name, tom.age)

tom.some = "some"   ##动态的给类增加录属性。

print(tom.some)

tom.show_attr_dict()


tom.name = 'tom3'
print(tom.name)


def pro(name):

    def get_name(instance):
        return instance.__dict__[name]

    def set_name(instance, value):
        instance.__dict__[name] = value

    return property(get_name, set_name)


class Test:
    def __init__(self, arg):
        self.arg = arg

    name = pro('name')


t = Test('hello')
t.name = 'kx'
print(t.name)
