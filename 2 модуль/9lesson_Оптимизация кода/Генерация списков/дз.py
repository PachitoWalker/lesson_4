# nums = []
# for i in range(1,11):
#     num = int(input("Введите " + str(i) + " число"))
#     nums.append(num)

# list1 = [i for i in nums if not(i%2)]
# list2 = [i for i in nums if i%2]

# print(list1)
# print(list2)

a = list((5,3,2,1,4))
a.sort()
a = tuple(a)
print(type(a),a)