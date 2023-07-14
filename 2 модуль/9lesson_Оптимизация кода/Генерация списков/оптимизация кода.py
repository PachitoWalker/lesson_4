import tkinter as tk

# def func(a,b, *args, **kwargs):
#     c = kwargs.get("c", 3)   # если в функщию передадут c (c = 4, например), то напечатать значение c, если нет, то напечатать 3 (с = 3)
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)

# func(1,2,123,431,5431,"dsf",[1,2],c=4,one=32,two="Два")   # позиционные - все последовательные эллементы, без знака =, именные - те которые со знаком =, как переменные (имеют имя)




#можно записывать так
age = 17

if age >= 18:
    is_allow = True
else:
    is_allow = False
print(is_allow)

#а можно так, это 1 из способов оптимизации и упрощения кода
is_allow = True if age >= 18 else False
print(is_allow)

#а можно так, это еще лучше
is_allow = age >= 18
print(is_allow)



#можно записать так
val = None   # None = 0 = False
if val == None:
    res = []
else:
    res = val
print(res)

#можно так
res = [] if val==None else val
print(res)


#а так еще лучше
val #= 13
res = 32332
res = val or res   # если val != None то res = val, иначе res=res
print(res)



#генератор списков
List = []
for i in range(1,101):
    if not(i%5):
        List.append(i)
print(List)

# а так проще
List = [i for i in range(1,101) if not(i % 5)]   #i%5 == 0 и not(i%5) равнозначны
print(List)

div_5list = [i**3 if i>50 else i for i in range(1,101) if i%5 == 0]
print(str(div_5list))


# генератор словарей
len_dict = {i : len(i) for i in ["orange", "green","blue","yellow"]}
print(len_dict)


div_30_31 = [i for i in range(0, 251) if not(i%30 and i%31)]
print(div_30_31)