#%%单词统计
text = """
Python is great. Python is easy. I love Python programming 
because Python is powerful and Python is fun!
"""
text = text.lower()
# 专为小写
text = text.replace(".","").replace(",", "").replace("!", "").replace("?", "")
print(text)
words = text.split()
# split 作用为字符串按照某个分隔符拆分成列表 split(",")即为按都好拆分
count = {}
# 穿件空字典
for word in words:
    # if word in count:
    #     count[word] += 1
    #     # 已存在次数加一
    # else:
    #     count[word] = 1
    # # 添加到字典里
    count[word] = count.get(word,0) + 1
    # .get查询key的value,若不存在就设为预定值
print(count)
#%% 成绩汇总
scores = {
    "小明": {"语文": 88, "数学": 92, "英语": 85},
    "小红": {"语文": 95, "数学": 78, "英语": 90},
    "小刚": {"语文": 76, "数学": 88, "英语": 82},
    "小丽": {"语文": 92, "数学": 85, "英语": 94},
}

# 请补充代码，打印：
# 1. 每个人 + 总分
for s in scores:
    total = sum(scores[s].values())
    print(f"{s} 总分：{total}")
# 2. 语文/数学/英语 的平均分（保留1位小数）
for subject in ["语文","数学","英语"]:
    #scores是个字典,他的value也是字典,s是字典  for s in scores.values() 正部分算个score[name]在括号里变元组,元组再求和得出
    avg = sum(s[subject] for s in scores.values()) / len(scores)
# for name in scores:
# print( scores[name]["语文"] )         
# 字典 套字典

# 3. 总分最高的学生姓名和分数
max_name = max(scores,key = lambda name: sum(scores[name].values()))
max_score = sum(scores[max_name].values())
print(f"总分最高：{max_name}，{max_score}分")
#%%
nums = [10, 25, 33, 42, 57, 68]
result = filter(lambda num: num > 50,nums)
a = list(result)
print(*a)

#%%
cities = ["beijing", "shanghai", "guangzhou", "shenzhen"]
Cities = list(map(lambda a: a.capitalize(),cities))
print(f"{Cities}")
#%%
scores = [78, 92, 85, 63, 97, 88, 74]
pass_score = list(filter(lambda score:score >= 60,scores))
result = list(map(lambda ele:f"{ele}分",pass_score))
print(result)
#%%
names = ["小明", "小红", "小刚"]
ages = [18, 20, 19]

new = map(lambda x,y:f"{x}{y}岁",names,ages)
print(list(new))
#%%