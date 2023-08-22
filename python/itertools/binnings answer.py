# https://stackoverflow.com/questions/11270991/divide-a-list-into-multiple-
# lists-based-on-a-bin-size/45991797#45991797

from itertools import groupby


class Binnings:
    def __init__(self, items):
        self.items = items

    @staticmethod
    def _key(x):
        return x[0]

    def group_by_first_digit_after_dot(self):
        grouped_binnings = {}
        tmp = tuple(tuple([round(x, 1), x]) for x in self.items)

        for key, group in groupby(sorted(tmp, key=self._key), key=self._key):
            grouped_binnings[key] = []
            for item in group:
                grouped_binnings[key].append(item[1])

        return grouped_binnings


binnings = Binnings(
    items=[
        -0.234,
        -0.04325,
        -0.43134,
        -0.315,
        -0.6322,
        -0.245,
        -0.5325,
        -0.6341,
        -0.5214,
        -0.531,
        -0.124,
        -0.0252,
    ]
)

print(binnings.group_by_first_digit_after_dot())
