from hashmap import HashMap
from node import Node


def main():

    hm = HashMap()

    hm.insert(1, 1)
    hm.insert(2, 1)
    hm.insert(3, 2)
    hm.insert(4, 2)
    hm.insert(5, 3)
    hm.insert(6, 3)
    hm.insert(7, 4)
    hm.insert(8, 4)

    hm.print_map()

    hm.insert(1, 999)
    hm.print_map()

    hm.delete(2)
    hm.print_map()

    # hm.insert(1, 5)
    # hm.print_map()
    # hm.insert(2, 3)
    # hm.print_map()


main()
