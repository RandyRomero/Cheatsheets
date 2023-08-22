# how to make an abstract method

import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def method_to_implement(self, input):
        """Method documentation"""
        return
