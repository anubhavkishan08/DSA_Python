def nextLargerElement(arr):
    st=[]
    nge_list=[-1]*len(arr)
    st.append(arr[-1])
    for i in range(len(arr)-2,-1,-1):
        while(len(st)>0 and st[-1]<=arr[i]):
            st.pop()
        if(len(st)==0):
            nge_list[i]=-1
        else:
            nge_list[i]=st[-1]
        st.append(arr[i])
    return nge_list
    


arr=[1,2,3,4,5]
print(nextLargerElement(arr))