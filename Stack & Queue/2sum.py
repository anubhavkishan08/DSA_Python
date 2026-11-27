nums = [1, 6, 2, 10, 3]
target = 7

element_idx=[]
for i in range(0,len(nums)):
    element_idx.append([nums[i],i])
    
nums.sort()

res=[-1,-1]

left=0
right=len(nums)-1
while left<right:
    if nums[left]+nums[right]<target:
        left+=1
    elif nums[left]+nums[right]>target:
        right-=1
    else:
        res[0]=nums[left]
        res[1]=nums[right]
        break

ans=[]
for i in range(0,len(element_idx)):
    if element_idx[i][0]==res[0] or element_idx[i][0]==res[1]:
        ans.append(element_idx[i][1])

print(ans)