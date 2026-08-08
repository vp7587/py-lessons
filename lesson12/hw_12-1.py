def prime_generator(end):
        source_list = list(range(1, end+1, 1))
        temp_list = list()
        for i in source_list:
            for j in source_list:
                if i % j == 0:
                    temp_list.append(j)
            if len(temp_list) == 2:
                yield i
            temp_list = list()


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
