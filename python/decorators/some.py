def power_factory(exp):
    def power(base):
        return base ** exp
    return power

square = power_factory(2)

print(square(4))
print(square(5))