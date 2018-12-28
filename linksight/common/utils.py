# -*- coding: utf-8 -*-

"""Utility methods common to the package"""


def urljoin(*args):
    """Join a set of strings for URL creation

    This method is commonly used by appending a URL to the `ENDPOINT`

    Parameters
    ----------
    string
        URL names to join

    Returns
    -------
    string
        The joined URL
    """
    return '/'.join(map(lambda a: a.strip('/'), args))
