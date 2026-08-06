# class shuaige:
#     def __init__(self,Name,Age):
#         self.name=Name
#         self.age=Age
# #这个类定义了对象的属性
#     def speak(self,speak):
#         print(f"{self.name}说{speak}")
# #这个类定义的方法
# shuaige1=shuaige("谢东宏",19)
# print(f"帅哥{shuaige1.name}的的年龄是{shuaige1.age}岁")
# shuaige1.speak("我是世界上最帅的人")

class student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0,"物理":0,"化学":0,"生物":0}

    def set_grade(self,course,grade):
        if course in self.grades.keys():
            self.grades[course]=grade
    def print_grades(self):
        print(f"学生{self.name}(学号：{self.student_id})的各科成绩是：")
        for course in self.grades.keys():
            print(f"{course}:{self.grades[course]}")
        print(f"学生{self.name}的总成绩是：")
        sum=0
        for course in self.grades.keys():
            sum+=self.grades[course]
        print(sum)

xie=student("谢东宏","52")
print(xie.name)
print(xie.student_id)
xie.set_grade("语文",122)
xie.set_grade("数学",121)
xie.set_grade("英语",136)
xie.set_grade("物理",67)
xie.set_grade("化学",93)
xie.set_grade("生物",89)
xie.print_grades()