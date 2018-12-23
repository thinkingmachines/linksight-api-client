# -*- coding: utf-8 -*-

"""Utility methods common to the package"""


def urljoin(*args):
    """Join a set of strings for URL creation"""
    return '/'.join(map(lambda a: a.strip('/'), args))
