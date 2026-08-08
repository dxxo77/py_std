f=open("D:/py项目/README.md","r", encoding="utf-8")
print(f.read())
f.close()
#or
# 修正后完整代码
# with open("D:/py项目/README.md","r", encoding="utf-8") as f:
#     print(f.read())

with open("D:/py项目/README.md","a", encoding="utf-8") as q:
     q.write("(基础)")