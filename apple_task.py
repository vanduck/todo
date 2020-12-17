import pickle
from datetime import datetime


with open('arr2.pkl', 'rb') as file:
    test_arr = pickle.load(file)


# example 1
def get_fixed_point(array):
    s = 0
    e = len(array) - 1
    while True:
        m = (e - s) // 2 + s
        if m > array[m]: s = m
        elif m < array[m]: e = m
        elif m != array[m]:
            return False
            break
        else:
            return m
            break


"""
def get_fixed_point(array):
    return separate(array, 0, len(array) - 1)

def separate(array, s, e):
    m = (e - s) // 2 + s
    if m > array[m]: separate(array, m, e)
    elif m < array[m]: separate(array,s, m)
    #elif m != array[m]: return False
    else: return m
"""


"""
    i = 0
    while i < array[i]:
        i += 1
    for index, num in enumerate(array, i):
        if index == num: return index
    return False
"""

start = datetime.now()
result = get_fixed_point(test_arr)
finish = datetime.now() - start
print(f'Result func1 => {result}  time: {finish}')

assert get_fixed_point(test_arr) == 648639
assert get_fixed_point([-3, -1, 0, 2, 3, 4, 6]) == 6
assert get_fixed_point([0, 2, 4, 6, 8, 10, 16]) == 0
assert get_fixed_point([-3, -1, 0, 2, 3, 5, 9]) == 5
assert get_fixed_point([-3, -1, 0, 2, 4, 7, 9]) == 4
assert get_fixed_point([-3, -1, 0, 2, 4, 7, 9, 25, 31]) == 4
assert get_fixed_point([-3, -1, 0, 2, 3, 5]) == 5
assert get_fixed_point([-3, -1, 0, 2, 3, 9]) is False
