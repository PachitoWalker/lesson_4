def func():
    return 12,45
print(type(func()))


some_list = list((1,2,3))
some_list[2] = 45
print(some_list, type(some_list))

some_tuple = tuple(some_list)
print(some_tuple, type (some_tuple))

some_dict = {(1,2,3):"Hello"}
print(some_dict[(1,2,3)])

tuple_2 = ([1,2,3,4], "1243235")
tuple_2[0].append(5)
print(tuple_2)

#is проверяет id элементов

x=13
y=13
y+=1

print(id(x), id(y))
print(x is y)   #id x == id y ? True/False

l = [1,2,3]
m = [1,2,3]   #print x is l? False

m = l   #print x is l? True   !!!при изменении l будет меняться и m, т.к теперь они ссылаютася на 1 ячеку памяти
print(id(l), id(m))   
print(l is m)