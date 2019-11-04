from itertools import groupby

things = [
    ("plant", "cucumber"),
    ("animal", "bear"),
    ("vehicle", "school bus"),
    ("animal", "duck"),
    ("vehicle", "speed boat"),
    ("plant", "cactus"),
]


def key(x): return x[0]


# groupby() only works on sorted iterables
for key, group in groupby(sorted(things, key=key), key=key):
    print(list(group))

# output
# [('animal', 'bear'), ('animal', 'duck')]
# [('plant', 'cucumber'), ('plant', 'cactus')]
# [('vehicle', 'school bus'), ('vehicle', 'speed boat')]

# from
# https://stackoverflow.com/questions/773/how-do-i-use-pythons-itertools-groupby
