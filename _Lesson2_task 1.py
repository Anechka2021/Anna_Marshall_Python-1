my_list = [(-2+0j), 2, 3.3, None, True, 'String', [5,6],
           (6,7,8), {8:'eight', 9: 'eight'},  {10,11},
           frozenset(), range(11), b'eleven', bytearray(b'twelve'),
           zip(*[(16,17), (17,18), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}){item} - {type(item)}")
