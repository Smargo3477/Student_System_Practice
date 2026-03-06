# 题目描述
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 你可以按任意顺序返回答案。

def func(nums,target):
    result = {}
    for a, b in enumerate(nums):
        if target - b in result:
            print(f"[{result[target - b]},{a}]")
            return
        else:
              result[b] = a
    return
    


nums = [4,5,6,3,5,7]
target = 9
func(nums,target)