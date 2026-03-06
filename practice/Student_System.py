
# %%
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math
#__init__初始化 
    
    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english} | 总分:{self.chinese + self.english + self.math}"
    
# __str__ 是 Python 类的内置魔法方法，用于自定义对象的字符串显示格式(默认打印只会打印对象地址)

    def update_score(self,chinese,math,english):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
#                      
# if __name__ == '__main__':
#     s1 = Student("牢大",90,90,80)
# 只有直接运行时才执行,代码,导入则不执行,测试代码
#print(s1)

class EduMangement:
    version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    #添加学生成绩 
    def add_student(self):
        name = input("请输入学生姓名")

        for s in self.student_list:
            if s.name == name:
                print("该学生已存在,添加失败")
                return
        
        chinese = int(input("请输入学生语文成绩"))
        english = int(input("请输入学生英语成绩"))
        math = int(input("请输入学生数学成绩"))

        if 0 <= chinese <=100 and 0 <= english <=100 and 0 <= math <=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("成绩信息错误,应为0-100")
            return

    #修改学生成绩
    def update_score(self):
        name = input("请输入学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"{s}")
                chinese = int(input("请输入修改后的学生语文成绩"))
                english = int(input("请输入修改后的学生英语成绩"))
                math = int(input("请输入修改后的学生数学成绩"))

                if 0 <= chinese <=100 and 0 <= english <=100 and 0 <= math <=100:
                    s.update_score(chinese,math,english)
                    print("修改成功")
                    print(f"{s}")
                    return
                else:
                    print("成绩信息错误,应为0-100")
                    return
        else:
            print("该学生不存在")
            return
            
    #删除学生成绩
    def delet_stu(self):
        name = input("请输入要删除的学生的姓名")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s) 
                print("删除成功")
                return               
        else:
            print("该学生不存在")
            return  
    #查询学生成绩 
    def search_stu(self):
        name = input("请输入要查询的学生的姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"{s}") 
                return               
        else:
            print("该学生不存在")
            return  
    #展示学生成绩
    def show_stu(self):
        for s in self.student_list:
            print(f"{s}")                   
        return
    #系统菜单
    def run(self):
        print(f"版本:{EduMangement.version}")

        while True:
            print("# # # # # # # # # #")
            print("1.添加学生成绩")
            print("2.修改学生成绩")
            print("3.删除学生成绩")
            print("4.查询指定学生成绩")
            print("5.展示全部学生成绩")
            print("6.退出系统")
            print("# # # # # # # # # #")

            choice = input("请输入操作选项")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_score()
                case "3":
                    self.delet_stu()
                case "4":
                    self.search_stu()
                case "5":
                    self.show_stu()
                case "6":
                    print("退出中")
                    break  
                case _:
                    print("操作指令错误")
# 创建菜单  

edu_mangement = EduMangement()
edu_mangement.run()

# %%
