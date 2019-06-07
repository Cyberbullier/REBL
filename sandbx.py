"""
fdfd
"""
import typing

class Dog:
    """fdfddfdf"""
    def __init__(self, breed, age, weight):
        self.breed= breed
        self.age = age
        self.weight = weight

    def is_healthy(self):
        """

        :return:
            """

        return 1<=self.weight<=100


def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)




if __name__ == '__main__':
    # breed, age, weight, weight_1 = "kira", 666666, 55, 'lofdfdfkjd'
    # dog = Dog(breed, age, weight_1)
    # print(dog.is_healthy())
    import collections
    print(fib(3))