# %%
while True:
    print("1.添加学生成绩")
    print("2.修改学生成绩")
    print("3.删除学生成绩")
    print("4.查询指定学生成绩")
    print("5.展示全部学生成绩")
# 创建菜单
# %%
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math
        
    
    def __str__(self):
        return{f"姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english} | 总分:{self.chinese + self.english + self.math}"}
    
    def update_score(self,chinese,math,english):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
                     
if __name__ == '__main__':
    s1 = Student("牢大",90,90,80)

print(s1)
# %%
