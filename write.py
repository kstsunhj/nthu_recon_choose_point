result = ['','','']
path = r'path\to\txt'
with open(path, 'r') as f:
    nums = f.read().split()
    
    for i in range(0, len(nums), 3):
        if i: result[0]+=','
        result[0]+=nums[i]
    result[0]+='\n'
    for i in range(1, len(nums), 3):
        if i != 1: result[1]+=','
        result[1]+=nums[i]
    result[1]+='\n'
    for i in range(2, len(nums), 3):
        if i != 2: result[2]+=','
        result[2]+=nums[i]
with open(path, 'w') as f:
    f.writelines(result) 