from enum import IntFlag, auto

# describe all our rights
class Rights(IntFlag):
    read = auto()   # 2**0 = 1   0001
    write = auto()  # 2**1 = 2   0010
    delete = auto()  # 2**2 = 4  0100

    # right + write = 1 + 2 = 3 = 0011

class User:

    def __init__(self, name, rights = Rights(0)):
        self.name = name
        self.rights = rights

    def __str__(self):
        if self.rights not in Rights:
            self.rights = None
        return f"{self.name} has the following rights: {self.rights}"


paul = User('Paul')

print(paul.rights)
# user1 = Rights.read
# print(user1)
# print(user1.value)
# user1 |= Rights.write
# print(user1)
# print(user1.value)
#
# print(Rights.write in user1)
# print(Rights.delete in user1)