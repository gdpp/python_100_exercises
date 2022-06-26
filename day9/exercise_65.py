# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

for x in [2, 4, 5, 6, 8]:
    assert x % 2 == 0, "{} is not an even number".format(x) 