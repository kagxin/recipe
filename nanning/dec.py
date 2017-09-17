# from funcy import silent, ignore, suppress
from functools import wraps
import json
from functools import reduce, namedtuple

def ignore(errors, default=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                return default
        return wrapper
    return decorator

def silent(func):

    return ignore(Exception)(func)

class suppress(object):

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):

        return exctype is not None and issubclass(exctype, self._exceptions)


id = silent(int)('SF')

with suppress(ValueError, TypeError):
    data = json.loads('{"helo":2}')
    print(data)
    print(data)

from fn import _

from functools import partial, update_wrapper, wraps
from inspect import getargspec

def identity(arg):
    return arg

class F(object):
    """Provide simple syntax for functions composition
    (through << and >> operators) and partial function
    application (through simple tuple syntax).

    Usage example:

    >>> func = F() << (_ + 10) << (_ + 5)
    >>> print(func(10))
    25
    >>> func = F() >> (filter, _ < 6) >> sum
    >>> print(func(range(10)))
    15
    """

    __slots__ = "f",

    def __init__(self, f=identity, *args, **kwargs):
        self.f = partial(f, *args, **kwargs) if any([args, kwargs]) else f

    @classmethod
    def __compose(cls, f, g):
        """Produces new class intance that will
        execute given functions one by one. Internal
        method that was added to avoid code duplication
        in other methods.
        """
        return cls(lambda *args, **kwargs: f(g(*args, **kwargs)))

    def __ensure_callable(self, f):
        """Simplify partial execution syntax.
        Rerurn partial function built from tuple
        (func, arg1, arg2, ...)
        """
        return self.__class__(*f) if isinstance(f, tuple) else f

    def __rshift__(self, g):
        """Overload >> operator for F instances"""
        return self.__class__.__compose(self.__ensure_callable(g), self.f)

    def __lshift__(self, g):
        """Overload << operator for F instances"""
        return self.__class__.__compose(self.f, self.__ensure_callable(g))

    def __call__(self, *args, **kwargs):
        """Overload apply operator"""
        return self.f(*args, **kwargs)


def curried(func):
    """A decorator that makes the function curried

    Usage example:

    >>> @curried
    ... def sum5(a, b, c, d, e):
    ...     return a + b + c + d + e
    ...
    >>> sum5(1)(2)(3)(4)(5)
    15
    >>> sum5(1, 2, 3)(4, 5)
    15
    """
    @wraps(func)
    def _curried(*args, **kwargs):
        f = func
        count = 0
        while isinstance(f, partial):
            if f.args:
                count += len(f.args)
            f = f.func

        spec = getargspec(f)

        if count == len(spec.args) - len(args):
            return func(*args, **kwargs)

        para_func = partial(func, *args, **kwargs)
        update_wrapper(para_func, f)
        return curried(para_func)

    return _curried
Student = namedtuple('Student', ['id', 'ans'])

QUIZE = 10


func = F() >> (_+5) >> (_+5)
print(func(10))
func = F() >> (filter, lambda x:x<6) >> sum

print(func(range(10)))

from fn.op import zipwith
from fn import Stream
from fn.iters import drop
import operator

s = Stream() << range(10)
s = Stream()
s << [0, 1] << map(operator.add, s, drop(1, s))
print(s[3])

from fn.monad import Option
from operator import methodcaller
from fn.monad import optionable


class Request(dict):
    @optionable
    def parameter(self, name):
        return self.get(name, None)


r = Request(testing="Fixed", empty="   ")

fixed = r.parameter("testing") \
        .map(methodcaller("strip")) \
        .filter(len) \
        .map(methodcaller("upper")) \
        .get_or("")

print(fixed)

print(list(zipwith(_+_)(range(10), range(10))))

def zip_with(func):
    def wrapper(lst, lst2):
        return map(func, lst, lst2)
    return wrapper
import traceback
def supperss2(*exceptions):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions:
                traceback.print_exc()
                return None
        return wrapper
    return  wrapper2


print(list(zip_with(_+_)(range(10), range(10))))


@supperss2(ValueError)
def test():
    raise ValueError

test()
print('test')
print('test')