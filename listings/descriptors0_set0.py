class TracedProperty:
    """Keep count of how many times an attribute changed its value"""

    def __set_name__(self, owner, name):
        self.name = name
        self.count_name = f'count_{name}'

    def __set__(self, instance, value):
        try:
            current_value = instance.__dict__[self.name]
        except KeyError:
            instance.__dict__[self.count_name] = 0
        else:
            if current_value != value:
                instance.__dict__[self.count_name] += 1

        instance.__dict__[self.name] = value


class Traveller:
    """
    >>> tourist = Traveller('John Smith')
    >>> tourist.city = 'Barcelona'
    >>> tourist.country = 'Spain'

    >>> tourist.count_city
    0
    >>> tourist.count_country
    0

    >>> tourist.city = 'Stockholm'
    >>> tourist.country = 'Sweden'
    >>> tourist.count_city
    1
    >>> tourist.count_country
    1
    >>> tourist.city = 'Gothenburg'
    >>> tourist.count_city
    2
    >>> tourist.count_country
    1
    >>> tourist.country = 'Sweden'
    >>> tourist.count_country
    1
    """
    city = TracedProperty()
    country = TracedProperty()

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
