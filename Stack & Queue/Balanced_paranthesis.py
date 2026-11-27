def isValid(s: str) -> bool:
    str_list=[]
    if(len(s)==0):
        return True
    str_list.append(s[0])
    for i in range(1,len(s)):
        if len(str_list)!=0 and str_list[-1]=='(' and s[i]==')':
            str_list.pop()
        elif len(str_list)!=0 and str_list[-1]=='{' and s[i]=='}':
            str_list.pop()
        elif len(str_list)!=0 and str_list[-1]=='[' and s[i]==']':
            str_list.pop()
        else:
            str_list.append(s[i])
    return len(str_list) == 0



str='[{}}]'

print(isValid(str))    