#!/usr/bin/env python

"""
Crossover base.
"""
import abc

import six

from ag_frame import base_item


@six.add_metaclass(abc.ABCMeta)
class BaseCrossover(base_item.BaseItem):
    """Base Crossover."""

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    NAME = "Base"

    # pragma pylint: disable=unused-argument
    def __init__(self, *args, **kwargs):
        """Initializa the arguments."""

    @abc.abstractmethod
    def crossover(self, arg1, arg2):
        """Return a list with the new crossoverd items."""
