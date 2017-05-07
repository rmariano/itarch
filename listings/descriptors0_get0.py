class Resolution:
    """Represents the resolution for a video display. In case there is no
    resolution set, return a default value, previously indicated.
    """
    def __init__(self, attr_name, default_resolution):
        self.attr_name = attr_name
        self.default_resolution = default_resolution

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.default_resolution


class VideoDriver:
    """Contains multiple display devices, each one with a resolution
    configured. If a resolution is not set for a device, return a default one,
    provided by this class, as a fallback.

    >>> media = VideoDriver()
    >>> media.tv
    (1024, 768)
    >>> media.tv = (4096, 2160)
    >>> media.tv
    (4096, 2160)
    >>> del media.tv
    >>> media.tv
    (1024, 768)
    >>> media.screen
    (1920, 1080)
    >>> VideoDriver.tv  # doctest: +ELLIPSIS
    <__main__.Resolution object at 0x...>
    """
    tv = Resolution('tv', (1024, 768))
    screen = Resolution('screen', (1920, 1080))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
