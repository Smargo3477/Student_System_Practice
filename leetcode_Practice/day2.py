#%%
def func (nums,val):
    b = 0
    for a in range(len(nums)):
        if nums[b] == val:
           del nums[b] 

        else:
            b += 1

    print(nums)
nums = [3,3,2,2]
val = 3
func(nums,val)
#%%
def func (nums,val):
    a = 0
    for b in range(len(nums)):
        if nums[b] != val:
            nums[a] = nums[b]
            a += 1
    return a
nums = [3,3,2,2]
val = 3
new_len = func (nums,val)
print(nums[:new_len])
#%%