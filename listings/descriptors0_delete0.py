"""An example of a descriptor with a ``__delete__()`` method.
The code is for illustration purposes only, and it does not correspond to any
actual implementation.
"""


class ProtectedAttribute:
    """A class attribute that can be protected against deletion"""

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Can't delete {self.name} for {instance!s}")


class ProtectedUser:
    """
    >>> usr = ProtectedUser('jsmith', '127.0.0.1')
    >>> usr.username
    'jsmith'
    >>> del usr.username
    Traceback (most recent call last):
    ...
    AttributeError: Can't delete username for ProtectedUser[jsmith]
    >>> usr.location
    '127.0.0.1'
    >>> del usr.location
    >>> usr.location
    Traceback (most recent call last):
    ...
    AttributeError: 'ProtectedUser' object has no attribute 'location'
    """
    username = ProtectedAttribute()

    def __init__(self, username, location):
        self.username = username
        self.location = location

    def __str__(self):
        return f"{self.__class__.__name__}[{self.username}]"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
