"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""


def common(list1, list2):
    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    >>> common(['a'], ['a'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'a', 'z', 'c'])
    ['a', 'c']
    >>> common(['a', 'b', 'c'], ['x', 'y', 'z'])
    []
    >>> common(['a', 'a', 'b'], ['a', 'a', 'x'])
    ['a']
    """
    # pass
    new_list = []
    for i in list1:
        for j in list2:
            if i==j and i not in new_list:
                new_list.append(i)
    return new_list
    """
    You implement this function.  Don't forget to remove the 'pass' statement above.
    """


def main():
    print("common(['a'], ['a']) returns: ")
    print(common(['a'], ['a']))                             # should print ['a']
    print("common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']) returns:")
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print("common(['a', 'b', 'c'], ['x', 'y', 'z']) returns:")
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print("common(['a', 'b', 'c'], ['a', 'a', 'x']) returns:")
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']


if __name__ == '__main__':
    main()
