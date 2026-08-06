import math
# usr=float(input())+10
# if usr>20:
#     print("我真帅")
# elif usr<20 and usr>10:
#     print("我不帅")
# else:
#     print("我真丑")
cont={"张":134,
      "谢":136,
      "里":111}
print(cont)
cont[("小帅")]=145
print(cont)
cont[("小帅","xiaomei","sss")]=155
print(cont)
del cont["小帅"]
print(cont)
for i in cont.keys():
    print(cont[i])


# list=["帅","丑"]
# list.extend([5,9,456])
# print(list)
# list.remove(456)
# print(list)
# cum=math.log2(8)
# wo="7123456789"[5]
# print(wo,cum)
# print(type(None),usr)