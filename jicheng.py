# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#
#     def print_info(self):
#         print(self.name)
#         print(self.id)
#
# class FULL(Employee):
#     def __init__(self,name,id,mouthly_salary):
#         super().__init__(name,id)#调用父类
#         self.mouthly_salary=mouthly_salary
#
#     def calculate_salary(self):
#         return self.mouthly_salary
#
# class Partime(Employee):
#     def __init__(self,name,id,daily_salary,work_days):
#         super().__init__(name,id)
#         self.daily_salary=daily_salary
#         self.work_days=work_days
#
#     def calculate_salary(self):
#         return self.daily_salary*self.work_days
#
# xiedonghong=FULL("Xiedonghong",1,15000)
# xiedonghong.print_info()
# print(xiedonghong.calculate_salary())
#
# lirunzhi=Partime("Lirunzhi",2,500,25)
# lirunzhi.print_info()
# print(lirunzhi.calculate_salary())

class A:
    def __init__(self):
        print("A初始化")

class B(A):
    def __init__(self):
        super().__init__()
        print("B初始化")

class C(A):
    def __init__(self):
        super().__init__()
        print("C初始化")

class D(C,B):
    def __init__(self):
        super().__init__()

d = D()
# 输出顺序：A → C → B，A只执行一次类重复构造，浪费资源