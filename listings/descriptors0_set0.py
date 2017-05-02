class TracedProperty:
    """Keep count of how many times a property changed its value"""

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
    >>> me = Traveller()
    >>> me.city = 'Barcelona'
    >>> me.country = 'Spain'
    >>> me.count_city
    0
    >>> me.count_country
    0

    >>> me.city = 'Stockholm'
    >>> me.country = 'Sweden'
    >>> me.count_city
    1
    >>> me.count_country
    1

    >>> me.city = 'Kiruna'
    >>> me.count_city
    2
    >>> me.count_country
    1
    >>> me.country = 'Sweden'
    >>> me.count_country
    1
    """
    city = TracedProperty()
    country = TracedProperty()
